// ================================
// NetWorth Vault
// Version 0.1.0
// ================================

// ---------- Login ----------

const loginForm = document.querySelector("form");

if (
    loginForm &&
    window.location.pathname.includes("login")
) {

    loginForm.addEventListener("submit", function (e) {

        e.preventDefault();

        localStorage.setItem("loggedIn", "true");

        window.location.href = "dashboard.html";

    });

}

// ---------- Register ----------

if (
    loginForm &&
    window.location.pathname.includes("register")
) {

    loginForm.addEventListener("submit", function (e) {

        e.preventDefault();

        alert("Account created successfully.");

        window.location.href = "login.html";

    });

}

// ---------- Logout ----------

const logoutButton = document.querySelector("nav button");

if (
    logoutButton &&
    window.location.pathname.includes("dashboard")
) {

    logoutButton.addEventListener("click", function () {

        localStorage.removeItem("loggedIn");

        window.location.href = "index.html";

    });

}

// ---------- Protect Dashboard ----------

if (
    window.location.pathname.includes("dashboard")
) {

    const loggedIn = localStorage.getItem("loggedIn");

    if (loggedIn !== "true") {

        window.location.href = "login.html";

    }

}
