function validar_usuario() {

    var usuario = "user"; //Verificar con la base de datos
    var usuarioNuevo = document.getElementById("user").value;
    var clave_nueva = document.getElementById("newPass").value;
    var clave_confirmacion = document.getElementById("confirmPass").value;
    if (usuario == usuarioNuevo) {
        alert("Usuario ya registrado, digite uno diferente.");
    } else {
        if (clave_nueva == clave_confirmacion) {
            alert("¡Registro exitoso!");
            //Guardar clave en la base de datos
            location.replace("/login"); /*NO ESTAMOS SEGUROS DE ESTE /Login*/
        } else {
            alert("Revise la clave y la confirmación.");
        }
        return false;
    }

}