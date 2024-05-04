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
    const url = "/comentarios/comentarios_json";

    showLoading();

    $.getJSON(url, function (data) {
      tableBody.innerHTML = "";
      let foundResults = false; // Variable para rastrear si se encontraron resultados

      data.comments.forEach((comment) => {
        if (
          comment.id.toString().includes(searchTerm) ||
          comment.comment.toLowerCase().includes(searchTerm) ||
          comment.create_date.toLowerCase().includes(searchTerm)
        ) {
          const row = document.createElement("tr");
          row.innerHTML = `
          <td>${comment.id}</td>
          <td>${comment.comment}</td>
          <td>${comment.create_date}</td>
          <td><button class="btn btn-editar editar" id="edit-button" data-comment-id="comment.id">Editar</button></td>
          `;
          tableBody.appendChild(row);
          foundResults = true;
        }
      });

      if (!foundResults) {
        const noResultsRow = document.createElement("tr");
        noResultsRow.innerHTML = `
                <td colspan="4" style="text-align:center;">No se encontraron resultados</td>
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
