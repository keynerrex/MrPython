document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("change_passsword");
  const loadingContainer = document.getElementById("loading-container");
  const contentSection = document.getElementById("content-section");

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
  showLoading();
  setTimeout(hideLoading(), 500);

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const currentPassword = document.getElementById("current_password").value;
    const newPassword = document.getElementById("new_password").value;
    const verifyPassword = document.getElementById("verify_password").value;
    const csrfToken = document.getElementById("csrf_token").value;
    showLoading();
    changePassword(currentPassword, newPassword, verifyPassword, csrfToken);
  });

  function cleanInput() {
    const currentPasswordInput = document.getElementById("current_password");
    currentPasswordInput.value = "";
    const newPasswordInput = document.getElementById("new_password");
    newPasswordInput.value = "";
    const verifyPasswordInput = document.getElementById("verify_password");
    verifyPasswordInput.value = "";
  }

  function changePassword(
    currentPassword,
    newPassword,
    verifyPassword,
    csrfToken
  ) {
    const url = "/contraseña/cambiar-contraseña";
    $.ajax({
      url: url,
      type: "POST",
      contentType: "application/json; charset=utf-8",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
      },
      data: JSON.stringify({
        current_password: currentPassword,
        new_password: newPassword,
        verify_password: verifyPassword,
      }),
    })
      .done(function (response) {
        Swal.fire({
          title: "Contraseña cambiada",
          text: response.success,
          icon: "success",
        });
        cleanInput();
        console.log(response.success);
      })
      .fail(function (xhr, status, error) {
        if (xhr.responseText) {
          const response = JSON.parse(xhr.responseText);
          Swal.fire({
            title: "Error al cambiar la contraseña",
            text: response.error,
            icon: "error",
          });
          console.error("Ha ocurrido un error: ", response.error);
        }
      })
      .always(function () {
        hideLoading();
      });
  }
});
function togglePassword(inputId) {
  let passwordInput = document.getElementById(inputId);
  let toggleButton = document.getElementById(`toggle_${inputId}`);

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleButton.classList.remove("fa-eye");
    toggleButton.classList.add("fa-eye-slash");
  } else {
    passwordInput.type = "password";
    toggleButton.classList.remove("fa-eye-slash");
    toggleButton.classList.add("fa-eye");
  }
}
