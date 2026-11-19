
(function () {
    function initializePage() {

        // Initialize Lucide icons
        if (window.lucide) {
            lucide.createIcons();
        }

        // Mobile sidebar
        const menuToggle = document.getElementById("menuToggle");
        const sidebar = document.getElementById("sidebar");

        if (menuToggle && sidebar) {
            menuToggle.onclick = function () {
                sidebar.classList.toggle("open");
            };
        }

        // Theme toggle
        const themeToggle = document.getElementById("themeToggle");

        function applyTheme(theme) {
            document.documentElement.setAttribute("data-theme", theme);

            try {
                localStorage.setItem("complaintIQTheme", theme);
            } catch (error) {
                console.warn("Could not save theme preference:", error);
            }

            if (themeToggle) {
                themeToggle.innerHTML = `
                    <i data-lucide="${theme === "dark" ? "sun" : "moon"}"></i>
                    <span>${theme === "dark" ? "Light mode" : "Dark mode"}</span>
                `;

                themeToggle.setAttribute(
                    "aria-label",
                    theme === "dark" ? "Switch to light mode" : "Switch to dark mode"
                );

                if (window.lucide) {
                    lucide.createIcons();
                }
            }
        }

        // Load saved theme
        let savedTheme = "light";

        try {
            savedTheme = localStorage.getItem("complaintIQTheme") || "light";
        } catch (error) {
            console.warn("Could not read saved theme:", error);
        }

        applyTheme(savedTheme);

        // Toggle on every click
        if (themeToggle) {
            themeToggle.onclick = function (event) {
                event.preventDefault();

                const currentTheme =
                    document.documentElement.getAttribute("data-theme") || "light";

                const newTheme =
                    currentTheme === "dark" ? "light" : "dark";

                applyTheme(newTheme);
            };
        }
    }

    // Works whether the script loads before or after DOMContentLoaded
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initializePage);
    } else {
        initializePage();
    }
})();
