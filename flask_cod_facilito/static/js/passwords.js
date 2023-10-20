
  function togglePassword(inputId) {
    let passwordInput = document.getElementById(inputId);
    let toggleButton = document.getElementById(`toggle_${inputId}`);
    
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      toggleButton.classList.remove("far", "fa-eye");
      toggleButton.classList.add("far", "fa-eye-slash");
    } else {
      passwordInput.type = "password";
      toggleButton.classList.remove("far", "fa-eye-slash");
      toggleButton.classList.add("far", "fa-eye");
    }
  }
