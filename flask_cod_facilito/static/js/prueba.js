        // JavaScript para alternar el menú lateral
        document.getElementById("menu-toggle-btn").addEventListener("click", function () {
            const sidebar = document.getElementById("sidebar");
            const mainContent = document.querySelector(".main-content");

            if (sidebar.style.width === "250px") {
                sidebar.style.width = "0";
                mainContent.style.marginLeft = "0";
            } else {
                sidebar.style.width = "250px";
                mainContent.style.marginLeft = "250px";
            }
        });

        // Abre el menú lateral al cargar la página
        setTimeout(function () {
            const sidebar = document.getElementById("sidebar");
            const mainContent = document.querySelector(".main-content");

            sidebar.style.width = "250px";
            mainContent.style.marginLeft = "250px";
        }, 500);