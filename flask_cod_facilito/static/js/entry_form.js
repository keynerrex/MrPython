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

  showLoading();

  setTimeout(hideLoading, 1000);

  $("#login-form").submit(function (event) {
    event.preventDefault();
    showLoading();

    const formData = $(this).serialize();
    const csrfToken = $("#csrf_token").val();

    $.ajax({
      url: "/accesos/formulario-ingreso",
      type: "POST",
      contentType: "application/x-www-form-urlencoded",
      headers: {
        "X-CSRF-TOKEN": csrfToken,
      },
      data: formData,
      success: function (response) {
        if (response.success) {
          console.log("Registro exitoso:");
          $("body").html(response.html);
        } else {
          console.error("Error al registrar:", response.error);
          alert("Error al registrar: " + response.error);
          hideLoading();
        }
      },
      error: function (xhr, status, error) {
        let errorMessage = "Error al registrar. Por favor, inténtalo de nuevo.";
        if (xhr.responseJSON && xhr.responseJSON.error) {
          errorMessage = xhr.responseJSON.error;
        }
        console.error("Error al registrar:", errorMessage);
        alert(errorMessage);
        hideLoading();
      },
    });
  });
});
