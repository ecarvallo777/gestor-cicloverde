
function mostrarAyudante1(){
//Si la opcion con id Conocido_1 (dentro del documento > formulario con name fcontacto >     y a la vez dentro del array de Conocido) esta activada
if (document.getElementById('a1').checked) {
document.getElementById('ayudante1').style.display="block";
document.getElementById('ayudante2').style.display="none";}



if (document.getElementById('a2').checked) {
    //muestra (cambiando la propiedad display del estilo) el div con id 'desdeotro'
    document.getElementById('ayudante1').style.display="block";
    document.getElementById('ayudante2').style.display="block";

//por el contrario, si no esta seleccionada
} if(document.getElementById('a0').checked){
//oculta el div con id 'desdeotro'
document.getElementById('ayudante1').style.display="none";

document.getElementById('ayudante2').style.display="none";
}
}
