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

  // Mostrar la pantalla de carga antes de cargar el contenido
  showLoading();

  // Simular una carga inicial (puedes ajustar el tiempo según sea necesario)
  setTimeout(hideLoading, 1000);

  $("#login-form").submit(function (event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
    showLoading();
    // Obtener los datos del formulario
    const formData = $(this).serialize();
    const csrfToken = $("#csrf_token").val(); // Obtener el token CSRF del campo oculto

    // Enviar la solicitud AJAX
    $.ajax({
      url: "/iniciar",
      type: "POST",
      contentType: "application/x-www-form-urlencoded",
      headers: {
        "X-CSRF-TOKEN": csrfToken, // Enviar el token CSRF en el encabezado
      },
      data: formData,
      success: function (response) {
        if (response.success) {
          console.log("Inicio de sesión exitoso:");
          window.location.href = response.redirect_url;
        } else {
          console.error("Error al iniciar sesión:", response.error); // Mostrar el mensaje de error en la consola
          alert("Error al iniciar sesión: " + response.error); // Mostrar mensaje de error al usuario
          hideLoading();
        }
      },
      error: function (xhr, status, error) {
        console.error("Error al iniciar sesión:", xhr.responseJSON.error); // Mostrar la respuesta del servidor en la consola
        alert("Error al iniciar sesión: " + xhr.responseJSON.error); // Mostrar mensaje de error al usuario
        hideLoading(); // Ocultar la pantalla de carga si hay un error
      },
    });
  });
});
