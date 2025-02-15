$(document).ready(function () {
  const loadingContainer = document.getElementById("loading-container");
  const contentSection = document.getElementById("content-section");
  const form = document.getElementById("login-form");

  function showLoading() {
    if (loadingContainer) loadingContainer.style.display = "flex";
    if (contentSection) contentSection.style.display = "none";
  }

  function hideLoading() {
    if (loadingContainer) loadingContainer.style.display = "none";
    if (contentSection) contentSection.style.display = "block";
  }

  // Simulación de carga
  showLoading();
  setTimeout(hideLoading, 200);

  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const username = document.getElementById("username").value.trim();
      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();
      const csrfTokenElement = document.getElementById("csrf_token");

      if (!username || !email || !password) {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Todos los campos son necesarios.",
        });

        return;
      }

      if (!csrfTokenElement) {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Error en el token de verificación.",
        });
        return;
      }

      const csrfToken = csrfTokenElement.value;
      registerUser(username, email, password, csrfToken);
    });
  }

  function registerUser(username, email, password, csrfToken) {
    const url = "/accesos/formulario-ingreso";

    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
        ModuleCharge: "This module is charged",
      },
      data: JSON.stringify({ username, email, password }),
      beforeSend: function () {
        showLoading();
      },
      success: function (response) {
        console.log("Usuario agregado:", response);
        Swal.fire({
          title: "Registro exitoso!",
          text: "Te redigiremos a la pagina de inicio de sesión!",
          icon: "success",
        });
        setTimeout(() => {
          window.location.href = "/iniciar";
        }, 2000);
      },
      error: function (xhr) {
        try {
          const response = JSON.parse(xhr.responseText); // Convertir JSON a objeto
          const errorMessage = response.error; // Obtener solo el mensaje de error

          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: errorMessage,
          });
        } catch (e) {
          console.error("Error al procesar la respuesta:", e);
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Ocurrió un error inesperado.",
          });
        }
      },
      complete: function () {
        hideLoading();
      },
    });
  }
});
