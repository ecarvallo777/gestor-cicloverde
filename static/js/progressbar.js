$(document).ready(function(){
    var current = 1,current_step,next_step,steps,stepscount;
    steps = $("fieldset").length;
    $(".next").click(function(){

        current_step = $(this).parent();

            if(current==2){
                var x = document.forms["regiration_form"]["browser"].value;

			    if( $("#regiration_form input[name='colacion']:radio").is(':checked') ) { 
                    next_step = $(this).parent().next();
                    next_step.show();
                    current_step.hide();
                    setProgressBar(++current);
				    } else{ if () 
					    alert("Seleccione colación.");  
                            }  
                }
                
            if(current==1){
                var horas_chofer = document.forms["regiration_form"]["horas_chofer"].value;
                var ayudante1 = document.forms["regiration_form"]["ayudante1"].value;
                var ayudante2 = document.forms["regiration_form"]["ayudante2"].value;


                
                var y = document.forms["regiration_form"]["direccion_servicio"].value;
                if (x ==""){
                    alert ("Ingrese nombre de representante");
                    
                    } else{ 
                        if (y ==""){
                            alert("Ingrese la direccion de servicio.");
                            } else {
                                    next_step = $(this).parent().next();
                                    next_step.show();
                                    current_step.hide();
                                    setProgressBar(++current);
                                    }
                                }
                            }





    });
    $(".previous").click(function(){
    current_step = $(this).parent();
    next_step = $(this).parent().prev();
    next_step.show();
    current_step.hide();
    setProgressBar(--current);
    });
    setProgressBar(current);
    // Change progress bar action
    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    .html(percent+"%");
    }
    });