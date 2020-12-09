
function mostrarGasto(){
    //Si la opcion con id Conocido_1 (dentro del documento > formulario con name fcontacto >     y a la vez dentro del array de Conocido) esta activada
    if (document.getElementById('check_asesorias').checked) {
    document.getElementById('asesorias').style.display="block";}
    else {
        document.getElementById('asesorias').style.display="none";
    }

    if (document.getElementById('check_administrativos').checked) {
        document.getElementById('administrativos').style.display="block";}
        else {
            document.getElementById('administrativos').style.display="none";
        }

    if (document.getElementById('check_produccion').checked) {
        document.getElementById('produccion').style.display="block";}
        else {
            document.getElementById('produccion').style.display="none";
        }

    
    
   
    }
    