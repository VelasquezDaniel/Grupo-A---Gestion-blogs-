function validar_contraseñas() {

  var clave_antiguaUsuario = document.getElementById("oldPass").value; //Modificar con la base de datos
  var clave_antigua = document.getElementById("oldPass").value;
  var clave_nueva = document.getElementById("newPass").value;
  var clave_confirmacion = document.getElementById("confirmPass").value;
  if (clave_antiguaUsuario != clave_antigua) {
      alert("La clave no corresponde a la registrada en el sistema.");
  } else {
      if (clave_nueva == clave_confirmacion) {
          alert("¡Cambio exitoso!");
      //Guardar clave en la base de datos
        location.replace("login.html");
        } else {
        alert("Revise la clave y la confirmación.");
        }
          return false;
}
}