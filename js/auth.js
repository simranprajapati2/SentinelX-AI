const password = document.getElementById("password");

if (password) {
    password.addEventListener("input", () => {
        console.log("Password Length:", password.value.length);
    });
}
