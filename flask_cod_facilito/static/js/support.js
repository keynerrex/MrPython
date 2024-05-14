document.addEventListener("DOMContentLoaded", function () {
  const tableBody = document.querySelector("#data-table tbody");
  const loadingContainer = document.getElementById("loading-container");
  const edit_button = document.getElementById("edit-button");
  let timeoutId;

  function showLoading() {
    // Mostrar la pantalla de carga
    loadingContainer.style.display = "flex";
    // Ocultar la tabla
    tableBody.style.display = "none";
  }

  function hideLoading() {
    // Ocultar la pantalla de carga después de 1 segundo
    setTimeout(() => {
      loadingContainer.style.display = "none";
      // Mostrar la tabla
      tableBody.style.display = "table-row-group";
    }, 500);
  }

  function fetchData(searchTerm) {
    const url = "/soporte/tickets_json";

    showLoading();

    $.getJSON(url, function (data) {
      tableBody.innerHTML = "";
      let foundResults = false; // Variable para rastrear si se encontraron resultados

      data.tickets.forEach((ticket) => {
        // Array de campos que quieres comparar con el término de búsqueda
        const fields = [
          ticket.id,
          ticket.username,
          ticket.email,
          ticket.ticket_manager_username,
          ticket.status,
          ticket.create_date,
        ];

        // Revisa si el término de búsqueda está en alguno de los campos
        const matchFound = fields.some(
          (field) =>
            field &&
            field.toString().toLowerCase().includes(searchTerm.toLowerCase())
        );

        if (matchFound) {
          const row = document.createElement("tr");
          row.innerHTML = `
              <td>${ticket.id}</td>
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
              <td><button class="btn btn-editar editar" id="edit-button" data-ticket-id="${
                ticket.id
              }">Editar</button></td>
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
      //función botón editar
      const editButtons = document.querySelectorAll(".btn-editar");
      editButtons.forEach((button) => {
        button.addEventListener("click", () => {
          for (let i = 0; i < 10; i++) {
            console.log("Generando edición...");
          }
          alert("Seguro");
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
      debounce(() => fetchData(searchTerm), 50); // Llama a fetchAndDisplayData después de un retraso de 50 ms
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

  // Llamar a la función al cargar la página
  fetchData("");
});
