function intTema(){
    var temaAtual = document.documentElement.getAttribute("data-bs-theme");
    if (temaAtual === "light") {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    } else {
        document.documentElement.setAttribute("data-bs-theme", "light");
    }
}


function senhaMostar() {
    var input = document.getElementById("senhauser");
    var eye = document.getElementById("eye");
    var eyeSlash = document.getElementById("eye-slash");
    if (input.type === "password") {
        input.type = "text";
        eye.style.display = "none";
        eyeSlash.style.display = "inline-block";
    } else {
        input.type = "password";
        eye.style.display = "inline-block";
        eyeSlash.style.display = "none";
    }
}
