$(document).ready(function () {
  function ajax_login() {
    $.ajax({
      url: "ajax-login",
      data: $("form").serialize(),
      type: "POST",
      succes: function (response) {
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  }

  $("#loginForm").submit(function (event) {
    event.preventDefault();
    ajax_login();
  });
});
