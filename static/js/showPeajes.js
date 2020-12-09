
function mostrarPeaje(){
    //Si la opcion con id Conocido_1 (dentro del documento > formulario con name fcontacto >     y a la vez dentro del array de Conocido) esta activada
    if (document.getElementById('check_lateral').checked) {
    document.getElementById('lateral').style.display="block";}
    else {
        document.getElementById('lateral').style.display="none";
    }

    if (document.getElementById('check_troncal').checked) {
        document.getElementById('troncal').style.display="block";}
        else {
            document.getElementById('troncal').style.display="none";
        }

    if (document.getElementById('check_pase').checked) {
        document.getElementById('pase').style.display="block";}
        else {
            document.getElementById('pase').style.display="none";
        }

    
    
   
    }
    