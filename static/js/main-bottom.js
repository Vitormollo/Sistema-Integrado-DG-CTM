function intTema(){
    var temaAtual = document.documentElement.getAttribute("data-bs-theme");
    var novo = (temaAtual === "light") ? "dark" : "light";
    document.documentElement.setAttribute("data-bs-theme", novo);
    // tenta salvar no localStorage; se não for possível (ex: modo privado), grava cookie como fallback
    try {
        localStorage.setItem('theme', novo);
    } catch (e) {
        document.cookie = 'theme=' + novo + '; path=/; max-age=' + 60*60*24*365;
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

// Inicialização mínima: aplica tema salvo no localStorage (ou cookie) ao carregar o script
(function(){
    function applyTheme(theme) {
        if (!theme) return;
        document.documentElement.setAttribute('data-bs-theme', theme);
    }

    function getSavedTheme() {
        try {
            var t = localStorage.getItem('theme');
            if (t) return t;
        } catch (e) {
            // localStorage inacessível
        }
        var m = document.cookie.match('(?:^|;)\\s*theme=([^;]+)');
        return m ? m[1] : null;
    }

    var saved = getSavedTheme();
    if (saved) {
        applyTheme(saved);
    } else if (!document.documentElement.getAttribute('data-bs-theme')) {
        // se nada definido, respeita preferência do sistema
        var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        applyTheme(prefersDark ? 'dark' : 'light');
    }
})();
