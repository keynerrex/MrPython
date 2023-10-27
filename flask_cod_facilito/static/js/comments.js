$(document).ready(function() {
    var currentPage = 1;
    var totalPages = null; // Variable para almacenar el número total de páginas

    // Función para cargar los comentarios inicialmente
    function loadInitialComments() {
        // Realiza una solicitud AJAX para cargar los comentarios de la página actual
        $.get("{{ url_for('comments.comentarios') }}?page=" + currentPage, function(data) {
            // Oculta la pantalla de carga
            $('#loading').hide();

            // Muestra la tabla de comentarios y llena los datos
            $('#comments-table').show();
            $('#pagination').show();

            // Llena la tabla con los comentarios
            $('#comments-table tbody').empty();
            $.each(data.comments, function(index, comment) {
                var row = '<tr>';
                row += '<td>' + ((currentPage - 1) * 5 + index + 1) + '</td>';
                row += '<td>' + comment.username + '</td>';
                row += '<td>' + comment.comment + '</td>';
                row += '<td>' + comment.create_date + '</td>';
                row += '</tr>';
                $('#comments-table tbody').append(row);
            });

            // Actualiza el número de página actual
            $('.current-page').text(currentPage);

            // Actualiza el número total de páginas
            totalPages = data.total_pages;

            // Habilita o deshabilita los botones de paginación según sea necesario
            if (currentPage === 1) {
                $('#prev-page').addClass('disabled');
            } else {
                $('#prev-page').removeClass('disabled');
            }
            if (currentPage === totalPages) {
                $('#next-page').addClass('disabled');
            } else {
                $('#next-page').removeClass('disabled');
            }
        });
    }

    // Carga los comentarios inicialmente al cargar la página
    loadInitialComments();

    // Maneja los botones de paginación
    $('#prev-page').click(function() {
        if (currentPage > 1) {
            currentPage--;
            loadComments(currentPage);
        }
    });

    $('#next-page').click(function() {
        if (currentPage < totalPages) {
            currentPage++;
            loadComments(currentPage);
        }
    });

    // Función para cargar los comentarios al cambiar de página
    function loadComments(page) {
        // Realiza una solicitud AJAX para cargar los comentarios de la página actual sin esperar
        $.get("{{ url_for('comments.comentarios') }}?page=" + page, function(data) {
            // Muestra la tabla con los comentarios
            $('#comments-table tbody').empty();
            $.each(data.comments, function(index, comment) {
                var row = '<tr>';
                row += '<td>' + ((currentPage - 1) * 5 + index + 1) + '</td>';
                row += '<td>' + comment.username + '</td>';
                row += '<td>' + comment.comment + '</td>';
                row += '<td>' + comment.create_date + '</td>';
                row += '</tr>';
                $('#comments-table tbody').append(row);
            });

            // Actualiza el número de página actual
            $('.current-page').text(currentPage);

            // Habilita o deshabilita los botones de paginación según sea necesario
            if (currentPage === 1) {
                $('#prev-page').addClass('disabled');
            } else {
                $('#prev-page').removeClass('disabled');
            }
            if (currentPage === totalPages) {
                $('#next-page').addClass('disabled');
            } else {
                $('#next-page').removeClass('disabled');
            }
        });
    }
});
