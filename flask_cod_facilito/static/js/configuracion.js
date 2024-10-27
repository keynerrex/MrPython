document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("reset_password");
  const loadingContainer = document.getElementById("loading-container");
  const contentSection = document.getElementById("content-section");

  // Función para mostrar el contenedor de carga
  function showLoading() {
    loadingContainer.style.display = "flex";
    contentSection.style.display = "none";
  }

  // Función para ocultar el contenedor de carga
  function hideLoading() {
    setTimeout(() => {
      loadingContainer.style.display = "none";
      contentSection.style.display = "block";
    }, 500);
  }
  showLoading();
  setTimeout(hideLoading(), 500);
  // Evento al enviar el formulario
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const usernameInput = document.getElementById("username");
    const username = usernameInput.value;
    const csrfToken = document.getElementById("csrf_token").value;

    // Mostrar carga antes de iniciar la solicitud
    showLoading();

    reset_pass(username, csrfToken);
    usernameInput.value = "";
  });

  function reset_pass(username, csrfToken) {
    const url = "/contraseña/restablecer-contraseña";

    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json; charset=utf-8",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
      },
      data: JSON.stringify({
        username: username,
      }),
      success: function (response) {
        Swal.fire({
          title: "Contraseña restablecida",
          text: `${response.success}`,
          icon: "success",
        });
        console.log("User updated successfully:", response);
        hideLoading(); // Ocultar carga en caso de éxito
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
      hideLoading(); // Ocultar carga en caso de fallo
    });
  }
});
