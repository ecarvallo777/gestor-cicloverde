$(document).ready(function(){
    var current = 1,current_step,next_step,steps,stepscount;
    steps = $("fieldset").length;
    $(".next").click(function(){

            current_step = $(this).parent();

            if(current==2){
                var x = document.forms["regiration_form"]["browser"].value;
                var horas_chofer = parseFloat(document.forms["regiration_form"]["horas_chofer"].value);
                var check_ayudante = document.forms["regiration_form"]["uno"].value;
                var horas_asistente_1 = parseFloat(document.forms["regiration_form"]["horas_asistente_1"].value);
                var horas_asistente_2 = parseFloat(document.forms["regiration_form"]["horas_asistente_2"].value);


                            if (horas_chofer>0){
                                if(check_ayudante=="0"){
                                    if( $("#regiration_form input[name='colacion']:radio").is(':checked') ) { 
                                        next_step = $(this).parent().next();
                                        next_step.show();
                                        current_step.hide();
                                        setProgressBar(++current);
                                        } else{
                                            alert("Seleccione colación.");  
                                                }

                                }
                                else{if (check_ayudante=="1"){
                                    if (horas_asistente_1>0){
                                        if( $("#regiration_form input[name='colacion']:radio").is(':checked') ) { 
                                            next_step = $(this).parent().next();
                                            next_step.show();
                                            current_step.hide();
                                            setProgressBar(++current);
                                            } else{
                                                alert("Seleccione colación.");  
                                                    }

                                    }else{alert("Seleccione horas de asistente 1.");

                                    }


                                    
                                }else{ if (check_ayudante=="2"){
                                    if (horas_asistente_1>0){
                                        if ( horas_asistente_2>0){
                                        if( $("#regiration_form input[name='colacion']:radio").is(':checked') ) { 
                                            next_step = $(this).parent().next();
                                            next_step.show();
                                            current_step.hide();
                                            setProgressBar(++current);
                                            } else{
                                                alert("Seleccione colación.");  
                                                    }
                                                }else { alert("Escriba horas de asistente 2.")}
                                    }else{alert("Escriba horas de asistente 1.");

                                    }

                                }
                                    }
                                    }
                                
                            }
                                else{alert("Escriba cantidad de horas de trabajo del chofer.")}





			      
                }
                
            if(current==1){
                var x = document.forms["regiration_form"]["browser"].value;

                var y = document.forms["regiration_form"]["fecha_requerida"].value;
                if (x ==""){
                    alert ("Ingrese nombre de organización.");
                    
                    } else{ 
                        if (y ==""){
                            alert("Ingrese la fecha de servicio.");
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