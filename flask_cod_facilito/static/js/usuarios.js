document.addEventListener("DOMContentLoaded", function () {
  const tableBody = document.querySelector("#data-table tbody");
  const loadingContainer = document.getElementById("loading-container");
  const modal = document.getElementById("forModal");
  const closeBtn = document.querySelector(".close");

  let timeoutId;

  closeBtn.onclick = function () {
    modal.style.display = "none";
  };

  // Llamar a la función al cargar la página
  fetchAndDisplayData("");

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

  function fetchAndDisplayData(searchTerm) {
    const url = "/usuarios/usuarios_json";

    showLoading();

    $.getJSON(url, function (data) {
      tableBody.innerHTML = "";
      let foundResults = false; // Variable para rastrear si se encontraron resultados

      data.all_users.forEach((user) => {
        //Campos admitidos en el buscador
        const fields = [
          user.id,
          user.username,
          user.email,
          user.rol,
          user.create_date,
        ];
        const matchFound = fields.some(
          (field) =>
            field &&
            field.toString().toLowerCase().includes(searchTerm.toLowerCase())
        );
        if (matchFound) {
          const row = document.createElement("tr");
          row.innerHTML = `
                        <td>${user.id}</td>
                        <td>${user.username}</td>
                        <td>${user.email}</td>
                        <td>${user.rol}</td>
                        <td>${user.create_date}</td>
                        <td>${
                          user.status === 1
                            ? "Activo"
                            : user.status === 0
                            ? "Inactivo"
                            : "Error de estado"
                        }</td>
                        <td><button class="btn btn-editar editar" data-user-id="${
                          user.id
                        }">Editar <i class="fa-solid fa-pen" style="color: #FFD43B;"></i></button></td>
                    `;
          tableBody.appendChild(row);
          foundResults = true; // Se encontraron resultados
        }
      });

      // Si no se encontraron resultados, agregar una fila con el mensaje
      if (!foundResults) {
        const noResultsRow = document.createElement("tr");
        noResultsRow.innerHTML = `
                    <td colspan="7" style="text-align:center;">No se encontraron resultados</td>
                `;
        tableBody.appendChild(noResultsRow);
      }

      hideLoading();
      //Función editar
      const editButtons = document.querySelectorAll(".btn-editar");
      editButtons.forEach((button) => {
        button.addEventListener("click", () => {
          const userID = button.getAttribute("data-user-id");
          loadUserData(userID);
          modal.style.display = "block";
        });
      });
    }).fail(function (error) {
      console.error("Error fetching data:", error);

      hideLoading();
    });
  }

  function loadUserData(userId) {
    const url = `/usuarios/usuarios/${userId}`;
    $.getJSON(url, function (user) {
      document.getElementById("userID").value = user.userID;
      document.getElementById("username").value = user.username;
      document.getElementById("email").value = user.email;
      document.getElementById("create_date").value = user.create_date;
      document.getElementById("status").value = user.status;

      // Cargar los managers en el select
      const rolID = document.getElementById("rol_id");
      rolID.innerHTML = ""; // Limpiar el select antes de llenarlo

      user.rols.forEach((rol) => {
        const option = document.createElement("option");
        option.value = rol.id;
        option.textContent = rol.rol;
        rolID.appendChild(option);
      });

      // Seleccionar la persona asignada
      rolID.value = user.rol_id;
    });
  }

  // Agregar evento al formulario del modal
  modal.addEventListener("submit", function (event) {
    event.preventDefault();

    const userId = document.getElementById("userID").value; // Obtener el ID del ticket
    const username = document.getElementById("username").value; // Obtener el ID del ticket
    const email = document.getElementById("email").value; // Obtener el ID del ticket
    const rol_id = parseInt(document.getElementById("rol_id").value); // Obtener el ID del ticket
    const status = parseInt(document.getElementById("status").value); // Obtener el estado

    udpateUserData(userId, username, email, rol_id, status); // Llamar a la función para actualizar el ticket
  });

  function udpateUserData(userId, username, email, rol_id, status) {
    const url = `/usuarios/usuarios/${userId}`;
    const csrfToken = document.getElementById("csrf_token").value; // Obtener el token CSRF del campo oculto

    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json; charset=utf-8",
      headers: {
        "X-CSRF-TOKEN": csrfToken, // Enviar el token CSRF en el encabezado
      },
      data: JSON.stringify({
        userId: userId,
        username: username,
        email: email,
        rol_id: rol_id,
        status: status,
      }),
      success: function (response) {
        console.log("User updated successfully:", response);
        // Cerrar el modal después de actualizar
        document.getElementById("forModal").style.display = "none";
        // Recargar los datos
        fetchAndDisplayData("");
      },
      error: function (xhr, status, error) {
        console.error("Error updating user:", xhr.responseText); // Mostrar la respuesta del servidor en la consola
        // Mostrar mensaje de error
        alert("Error al actualizar el usuario: " + xhr.responseText);
      },
    }).fail(function (xhr, status, error) {
      // Manejar errores de la solicitud AJAX
      console.error("Error updating user:", xhr.responseText); // Mostrar la respuesta del servidor en la consola
      // Mostrar mensaje de error
      alert("Error al actualizar el usuario: " + xhr.responseText);
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
      debounce(() => fetchAndDisplayData(searchTerm), 500); // Llama a fetchAndDisplayData después de un retraso de 50 ms
    });

  document
    .getElementById("report-button")
    .addEventListener("click", function () {
      for (let i = 0; i < 10; i++) {
        console.log("Generando reporte...");
      }
    });
});
