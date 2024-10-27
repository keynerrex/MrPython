$(document).ready(function () {
  const loadingContainer = document.getElementById("loading-container");
  const contentSection = document.getElementById("content-section");

  function showLoading() {
    loadingContainer.style.display = "flex";
    contentSection.style.display = "none";
  }

  function hideLoading() {
    loadingContainer.style.display = "none";
    contentSection.style.display = "block";
  }

  showLoading(); // Mostrar carga al cargar la página

  setTimeout(hideLoading, 1000); // Ocultar carga después de un tiempo (ajusta según necesites)

  $("#login-form").submit(function (event) {
    event.preventDefault();
    showLoading();
    const formData = $(this).serialize();
    const csrfToken = $("#csrf_token").val();

    $.ajax({
      url: "/iniciar",
      type: "POST",
      contentType: "application/x-www-form-urlencoded",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
      },
      data: formData,
    })
      .done(function (response) {
        console.log(`Codigo de respuesta: ${response.CodeResponse}`);
        console.log(response.success);
        window.location.href = response.redirect_url;
      })
      .fail(function (xhr) {
        let errorMessage = "Error al iniciar sesión.";
        if (xhr.responseJSON && xhr.responseJSON.error) {
          errorMessage += " " + xhr.responseJSON.error;
        }
        console.error("Error al iniciar sesión:", errorMessage);
        alert(errorMessage);
        hideLoading(); // Asegúrate de ocultar la carga aquí también
      });
  });
});
