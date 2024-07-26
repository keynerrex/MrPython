document.addEventListener("DOMContentLoaded", function () {
  const loadingContainer = document.getElementById("loading-container");
  const contentsection = document.getElementById("content-section");
  const form = document.getElementById("add_comment");
  showLoading();

  function showLoading() {
    loadingContainer.style.display = "flex";
    contentsection.style.display = "none";
  }

  function hideLoading() {
    setTimeout(() => {
      loadingContainer.style.display = "none";
      contentsection.style.display = "block";
    }, 500);
  }

  hideLoading();
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const csrfToken = document.getElementById("csrf_token").value;
    const commentInput = document.getElementById("comment");
    const comment = commentInput.value;
    add_comment(csrfToken, comment);
    commentInput.value = "";
    showLoading();
  });

  function add_comment(csrfToken, comment) {
    const url = "/comentarios/escribir-comentario";
    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json; charset=utf-8",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
      },
      data: JSON.stringify({
        comment: comment,
      }),
      success: function (response) {
        Swal.fire({
          title: "Comentario enviado",
          text: `${response.success}`,
          icon: "success",
        });
        console.log("Comentario agregado");
      },
    }).fail(function (xhr, status, error) {
      if (xhr.responseText) {
        const response = JSON.parse(xhr.responseText);
        Swal.fire({
          title: "Error en la operación",
          text: `${response.error}`,
          icon: "error",
        });
        console.error("Ha ocurrido un error: ", xhr.responseText);
      }
    });
    hideLoading();
  }
});
