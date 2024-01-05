document.addEventListener("DOMContentLoaded", function () {
    const tableBody = document.querySelector("#data-table tbody");
    const loadingContainer = document.getElementById("loading-container");


    function showLoading() {
        // Mostrar la pantalla de carga
        loadingContainer.style.display = "flex";
        // Ocultar la tabla
        tableBody.style.display = "none";
    }

    function hideLoading() {
        // Ocultar la pantalla de carga después de 1 segundo
        setTimeout(() => {
            loadingContainer.style.display = "none";
            // Mostrar la tabla
            tableBody.style.display = "table-row-group";
        }, 1000);
    }

    function fetchAndDisplayData(searchTerm) {
        const url = "/usuarios/usuarios_json";

        showLoading();
        /**
         *  Petición GET hacía la función de python que contiene el JSON de los usuarios
         */
        $.getJSON(url, function (data) {
            tableBody.innerHTML = "";

            data.all_users.forEach(user => {
                //Parámetros de busqueda username && email
                if (user.username.toLowerCase().includes(searchTerm) ||
                    user.email.toLowerCase().includes(searchTerm)) {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${user.id}</td>
                        <td>${user.username}</td>
                        <td>${user.email}</td>
                        <td>${user.rol === null ? 'Error de rol' : user.rol}</td>
                        <td>${user.create_date}</td>
                        <td>${user.status === 1 ? 'Activo' : user.status === 0 ? 'Inactivo ' : 'Error de estado'}</td>
                        <td> <button class="btn btn-editar editar" data-bs-toggle="modal" data-bs-target="#edit-user-modal">Editar</button> </td>
                    `;

                    tableBody.appendChild(row);
                }
            });

            hideLoading();
        })
        //En caso de error se mostrará el mensaje 
        .fail(function (error) {
            // Se prepara la tabla en blanco
            tableBody.innerHTML = "";
            const row = document.createElement("tr");
            //Se llena la tabla con el mensaje centrado
            row.innerHTML = `
            <td colspan="7" style="text-align: center;"> Ha ocurrido un error</td>
            `
            tableBody.appendChild(row);
            console.error("Error fetching data:", error);

            hideLoading();
        });
    }

    //Funcionalidad para el filtro de busqueda
    document.getElementById("search-input").addEventListener("input", function () {
        const searchTerm = this.value.toLowerCase();
        fetchAndDisplayData(searchTerm);
    });

    //Funcionalidad para genera reporte por excel
    document.getElementById("report-button").addEventListener("click", function () {
        for (let i = 0; i < 10; i++) {
            console.log("Generando reporte...");
        }
    });

    // Llamar a la función al cargar la página
    fetchAndDisplayData("");
});
