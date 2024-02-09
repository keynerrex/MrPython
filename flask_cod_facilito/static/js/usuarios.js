document.addEventListener("DOMContentLoaded", function () {
  const tableBody = document.querySelector("#data-table tbody");
  const loadingContainer = document.getElementById("loading-container");
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

  function fetchAndDisplayData(searchTerm) {
    const url = "/usuarios/usuarios_json";

    showLoading();

    $.getJSON(url, function (data) {
      tableBody.innerHTML = "";

      data.all_users.forEach((user) => {
        if (
          user.id.toString().includes(searchTerm) ||
          user.username.toLowerCase().includes(searchTerm) ||
          user.email.toLowerCase().includes(searchTerm)
        ) {
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
                          ? "Inactivo "
                          : "Error de estado"
                      }</td>
                      <td> <button class="btn btn-editar editar" data-bs-toggle="modal" data-bs-target="#edit-user-modal">Editar</button> </td>
                  `;

          tableBody.appendChild(row);
        }
      });

      hideLoading();
    }).fail(function (error) {
      console.error("Error fetching data:", error);

      hideLoading();
    });
  }

  function debounce(func, delay) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(func, delay);
}

document.getElementById("search-input").addEventListener("input", function () {
    const searchTerm = this.value.toLowerCase();
    debounce(() => fetchAndDisplayData(searchTerm), 50); // Llama a fetchAndDisplayData después de un retraso de 50 ms
});

  document
    .getElementById("report-button")
    .addEventListener("click", function () {
      for (let i = 0; i < 10; i++) {
        console.log("Generando reporte...");
      }
    });

  // Llamar a la función al cargar la página
  fetchAndDisplayData("");
});
