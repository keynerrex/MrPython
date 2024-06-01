document.addEventListener("DOMContentLoaded", function () {
  const tableBody = document.getElementById("table-body");
  const loadingContainer = document.getElementById("loading-container");
  const modal = document.getElementById("forModal");
  const closeBtn = document.querySelector(".close");

  closeBtn.onclick = function () {
    modal.style.display = "none";
  };

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
    const url = "/comentarios/comentarios_json";
    showLoading();

    $.getJSON(url, function (data) {
      tableBody.innerHTML = "";
      let foundResults = false;

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
                      <td><button class="btn btn-editar editar" data-comment-id="${comment.id}">Editar</button></td>
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

      const editButtons = document.querySelectorAll(".btn-editar");
      editButtons.forEach((button) => {
        button.addEventListener("click", () => {
          const commentID = button.getAttribute("data-comment-id");
          loadCommentData(commentID);
          modal.style.display = "block";
        });
      });
    }).fail(function (error) {
      console.error("Error fetching data:", error);
      hideLoading();
    });
  }

  function loadCommentData(commentID) {
    const url = `/comentarios/comentarios/${commentID}`;

    $.getJSON(url, function (comment) {
      document.getElementById("commentID").value = comment.commentID;
      document.getElementById("comment").value = comment.comment;
      document.getElementById("create_date").value = comment.create_date;
    });
  }

  function debounce(func, delay) {
    let timeoutId;
    return function () {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(func, delay);
    };
  }

  document
    .getElementById("search-input")
    .addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();
      debounce(() => fetchData(searchTerm), 500)();
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

  const modalForm = document.getElementById("modalForm");
  modalForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const commentID = document.getElementById("commentID").value;
    const comment = document.getElementById("comment").value;
    // Aquí puedes enviar los datos actualizados del comentario
    updateComment(commentID, comment);
    modal.style.display = "none";
  });

  function updateComment(commentID, comment) {
    const url = `/comentarios/comentarios/${commentID}`;
    const csrfToken = document.getElementById("csrf_token").value;

    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
      },
      data: JSON.stringify({
        comment: comment,
      }),
      success: function (response) {
        console.log("Comment updated successfully:", response);
        fetchData(""); // Recargar los datos después de actualizar
      },
      error: function (xhr, status, error) {
        console.error("Error updating comment:", xhr.responseText); // Mostrar la respuesta del servidor en la consola
        // Mostrar mensaje de error
        alert("Error al actualizar el comentario: " + xhr.responseText);
      },
    }).fail(function (xhr, status, error) {
      // Manejar errores de la solicitud AJAX
      console.error("Error updating comment:", xhr.responseText); // Mostrar la respuesta del servidor en la consola
      // Mostrar mensaje de error
      alert("Error al actualizar el comentario: " + xhr.responseText);
    });
  }
  fetchData("");
});
