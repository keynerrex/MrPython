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
    const formData = new FormData(form);
    add_comment(formData);
    showLoading();
    form.reset();
  });

  function add_comment(formData) {
    const url = "/comentarios/escribir-comentario";
    fetch(url, {
      method: "POST",
      contentType: "application/json; charset=utf-8",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert(data.message);
        } else {
          alert("Espera: " + data.message);
        }
        hideLoading();
      })
      .catch((error) => {
        console.error("Error: " + error);
        alert("Error al comentar");
        hideLoading();
      });
  }
});
