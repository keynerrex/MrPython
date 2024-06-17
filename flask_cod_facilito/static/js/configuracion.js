document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("reset_password");
  const loadingContainer = document.getElementById("loading-container");
  const contentSection = document.getElementById("content-section");

  showLoading();

  function showLoading() {
    loadingContainer.style.display = "flex";
    contentSection.style.display = "none";
  }

  function hideLoading() {
    setTimeout(() => {
      loadingContainer.style.display = "none";
      contentSection.style.display = "block";
    }, 500);
  }
  hideLoading();

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const usernameInput = document.getElementById("username");
    const username = usernameInput.value;
    const csrfToken = document.getElementById("csrf_token").value; // Obtener el token CSRF del campo oculto
    reset_pass(username, csrfToken);
    usernameInput.value = "";
    showLoading();
  });

  function reset_pass(username, csrfToken) {
    const url = "/contraseña/restablecer-contraseña";
    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json; charset=utf-8",
      headers: {
        "X-CSRF-TOKEN": csrfToken, // Enviar el token CSRF en el encabezado
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
