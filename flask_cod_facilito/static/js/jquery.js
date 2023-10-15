$(document).ready(function () {
    function ajax_login() {
      $.ajax({
        url: "/ajax-login", // Corregido el URL
        data: $("form").serialize(),
        type: "POST",
        success: function (response) { // Corregido "success"
          console.log(response);
        },
        error: function (error) {
          console.log(error);
        },
      });
    }
  
    $("#loginForm").submit(function (event) {
      ajax_login();
    });
  });
  