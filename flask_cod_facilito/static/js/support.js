document.addEventListener("DOMContentLoaded", function () {
  const tableBody = document.querySelector("#data-table tbody");
  const loadingContainer = document.getElementById("loading-container");
  let timeoutId;

  const modal = document.getElementById("forModal");
  const closeBtn = document.getElementsByClassName("close")[0];

  function showLoading() {
    loadingContainer.style.display = "flex";
    tableBody.style.display = "none";
  }

  function hideLoading() {
    setTimeout(() => {
      loadingContainer.style.display = "none";
      tableBody.style.display = "table-row-group";
    }, 500);
  }

  function fetchData(searchTerm) {
    const url = "/soporte/tickets_json";

    showLoading();

    $.getJSON(url, function (data) {
      tableBody.innerHTML = "";
      let foundResults = false;

      data.tickets.forEach((ticket) => {
        const fields = [
          ticket.id,
          ticket.username,
          ticket.email,
          ticket.ticket_manager_username,
          ticket.status,
          ticket.create_date,
        ];

        const matchFound = fields.some(
          (field) =>
            field &&
            field.toString().toLowerCase().includes(searchTerm.toLowerCase())
        );

        if (matchFound) {
          const row = document.createElement("tr");
          row.innerHTML = `
              <td id="ticketId">${ticket.id}</td>
              <td>${ticket.username}</td>
              <td>${ticket.details_error}</td>
              <td>${ticket.image_path}</td>
              <td>${ticket.email}</td>
              <td>${
                ticket.ticket_manager_username == null
                  ? "No hay persona asignada"
                  : ticket.ticket_manager_username
              }</td>

              <td>${
                ticket.status === 1
                  ? "Activo"
                  : ticket.status === 0
                  ? "Inactivo"
                  : "Error de estado"
              }</td>

              <td>${ticket.create_date}</td>
              <td><button class="btn btn-editar editar" data-ticket-id="${
                ticket.id
              }">Editar <i class="fa-solid fa-pen" style="color: #FFD43B;"></i></button></td>
            `;
          tableBody.appendChild(row);
          foundResults = true;
        }
      });

      if (!foundResults) {
        const noResultsRow = document.createElement("tr");
        noResultsRow.innerHTML = `
                  <td colspan="9" style="text-align:center;">No se encontraron resultados</td>
              `;
        tableBody.appendChild(noResultsRow);
      }

      hideLoading();

      const editButtons = document.querySelectorAll(".btn-editar");
      editButtons.forEach((button) => {
        button.addEventListener("click", function () {
          const ticketId = this.getAttribute("data-ticket-id");
          loadTicketData(ticketId);
          modal.style.display = "block";
        });
      });
    }).fail(function (error) {
      console.error("Error fetching data:", error);
      hideLoading();
    });
  }

  function debounce(func, delay) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(func, delay);
  }

  document
    .getElementById("search-input")
    .addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();
      debounce(() => fetchData(searchTerm), 50);
    });

  document.getElementById("report-button").addEventListener("click", () => {
    for (let i = 0; i < 10; i++) {
      console.log("Generando reporte...");
      Swal.fire({
        title: "Error!",
        text: "Do you want to continue",
        icon: "error",
        confirmButtonText: "Cool",
      });
    }
  });

  closeBtn.onclick = function () {
    modal.style.display = "none";
  };

  const form = document.getElementById("modalForm");
  form.onsubmit = function (event) {
    event.preventDefault();
    const ticket_manager_username = document.getElementById(
      "ticket_manager_username"
    ).value;
    const status = document.getElementById("status").value;
    console.log("ticket_manager_username:", ticket_manager_username);
    console.log("status:", status);
    modal.style.display = "none";
  };
  function loadTicketData(ticketId) {
    const url = `/soporte/ticket/${ticketId}`;

    $.getJSON(url, function (ticket) {
      document.getElementById("ticketID").value = ticket.ticketID;
      document.getElementById("username").value = ticket.username;
      document.getElementById("details_error").value = ticket.details_error;
      document.getElementById("email").value = ticket.email;
      document.getElementById("create_date").value = ticket.create_date;

      // Cargar los managers en el select
      const managerSelect = document.getElementById("ticket_manager_username");
      managerSelect.innerHTML = ""; // Limpiar el select antes de llenarlo

      ticket.managers.forEach((manager) => {
        const option = document.createElement("option");
        option.value = manager.id;
        option.textContent = manager.username;
        managerSelect.appendChild(option);
      });

      // Seleccionar la persona asignada
      managerSelect.value = ticket.ticket_manager_username;

      // Asignar el estado
      document.getElementById("status").value = ticket.status;
    });
  }

  // Agregar evento al formulario del modal
  const modalForm = document.getElementById("modalForm");
  modalForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const ticketId = document.getElementById("ticketID").value; // Obtener el ID del ticket
    const ticketManagerId = parseInt(
      document.getElementById("ticket_manager_username").value
    ); // Obtener el ID del manager seleccionado
    const status = parseInt(document.getElementById("status").value); // Obtener el estado

    updateTicket(ticketId, ticketManagerId, status); // Llamar a la función para actualizar el ticket
  });

  function updateTicket(ticketId, ticketManagerId, status) {
    const url = `/soporte/ticket/${ticketId}`;
    const csrfToken = document.getElementById("csrf_token").value; // Obtener el token CSRF del campo oculto

    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json",
      headers: {
        "X-CSRF-TOKEN": csrfToken, // Enviar el token CSRF en el encabezado
      },
      data: JSON.stringify({
        ticket_manager_id: ticketManagerId,
        status: status,
      }),
      success: function (response) {
        console.log("Ticket updated successfully:", response);
        // Cerrar el modal después de actualizar
        document.getElementById("forModal").style.display = "none";
        // Recargar los datos
        fetchData("");
      },
      error: function (xhr, status, error) {
        console.error("Error updating ticket:", xhr.responseText); // Mostrar la respuesta del servidor en la consola
        // Mostrar mensaje de error
        alert("Error al actualizar el ticket: " + xhr.responseText);
      },
    }).fail(function (xhr, status, error) {
      // Manejar errores de la solicitud AJAX
      console.error("Error updating ticket:", xhr.responseText); // Mostrar la respuesta del servidor en la consola
      // Mostrar mensaje de error
      alert("Error al actualizar el ticket: " + xhr.responseText);
    });
  }

  fetchData("");
});
