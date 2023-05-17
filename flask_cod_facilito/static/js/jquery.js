// $(document).ready(function () {
//   function ajax_login() {
//     $.ajax({
//       url: "ajax-login",
//       data: $("form").serialize(),
//       type: "POST",
//       succes: function (response) {
//         console.log(response);
//       },
//       error: function (error) {
//         console.log(error);
//       },
//     });
//   }

//   $("#loginForm").submit(function (event) {
//     ajax_login();
//   });
// });

// $(document).ready(function () {
//   function getComments() {
//     $.ajax({
//       url: "/comentarios-usuarios",
//       type: "GET",
//       success: function (response) {
//         var comments = [];

//         // Parsear el HTML de la respuesta para obtener los datos de los comentarios
//         var html = $.parseHTML(response);
//         $(html)
//           .find("tbody tr")
//           .each(function () {
//             var username = $(this).find("td:eq(0)").text().trim();
//             var comment = $(this).find("td:eq(1)").text().trim();

//             comments.push({
//               username: username,
//               comment: comment,
//             });
//           });

//         console.log(comments);
//         // Aquí puedes procesar los comentarios en formato JSON y mostrarlos en la página
//       },
//       error: function (error) {
//         console.log(error);
//       },
//     });
//   }

//   getComments();
// });
