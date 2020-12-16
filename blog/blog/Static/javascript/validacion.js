var intentos = 3;

function validar_formulario() {

    var nombre = document.getElementById("usuario").value;
    var clave = document.getElementById("password").value;
    if ((nombre == "usuario" && clave == "user") || (nombre == "admin" && clave == "admin")) {
        location.replace("dashboard.html");
    } else {
        if (intentos == 0) {
            alert("Se han acabado los intentos");
        } else {
            intentos = intentos - 1;
            alert("Intentos restantes: " + intentos);
            if (intentos == 0) {
                document.getElementById("usuario").disabled = true;
                document.getElementById("password").disabled = true;
                document.getElementById("submit").disabled = true;
            }
        }
    }

    return false;
}