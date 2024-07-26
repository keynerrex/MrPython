document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("formSupport");
  const loadingContainer = document.getElementById("loading-container");
  const contentSection = document.getElementById("content-section");
  showLoading();

  setTimeout(() => {
    hideLoading();
  }, 500);

  function showLoading() {
    loadingContainer.style.display = "flex";
    contentSection.style.display = "none";
  }

  function hideLoading() {
    loadingContainer.style.display = "none";
    contentSection.style.display = "block";
  }

  function create_ticket(formData) {
    url = "/soporte/enviar-soporte";
    fetch(url, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert("¡Ticket de soporte creado exitosamente!");
        } else {
          alert("Error: " + data.message);
        }
        hideLoading();
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Error al enviar el formulario.");
        hideLoading();
      });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(form);
    create_ticket(formData);
    showLoading();
    form.reset();
  });
});
