function validar_contraseñas()
{
 var nombre=document.getElementById("usuario").value;
 var clave=document.getElementById("password").value;
 if(nombre=="test" && clave=="test")
 {
    alert("Ingreso Exitoso");
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
    document.getElementById("button").disabled=true;
    document.getElementById("formulario").disabled=true;
   }
  }
 }
 
 return false;
}