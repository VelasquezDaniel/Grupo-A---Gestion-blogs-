var intentos=3;
function validar_formulario(){

 var nombre=document.getElementById("login-usuario").value;
 var clave=document.getElementById("login-contraseña").value;
 if(nombre=="user" && clave=="user")
 {
    location.replace("Dashboard.html");
 }
 else
 {
  if(intentos==0)
  {
    alert("Se han acabado los intentos");
  }
  else
  {
    intentos=intentos-1;
   alert("Intentos restantes: "+intentos);
   if(intentos==0)
   {
    document.getElementById("usuario").disabled=true;
    document.getElementById("password").disabled=true;
    document.getElementById("submit").disabled=true;
   }
  }
 }
 
 return false;
}