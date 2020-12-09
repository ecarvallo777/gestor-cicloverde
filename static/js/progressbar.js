$(document).ready(function(){
    var current = 1,current_step,next_step,steps,stepscount;
    steps = $("fieldset").length;
    $(".next").click(function(){
            current_step = $(this).parent();
            if(current==2){
			    if( $("#regiration_form input[name='colacion']:radio").is(':checked') ) {  
                    next_step = $(this).parent().next();
                    next_step.show();
                    current_step.hide();
                    setProgressBar(++current);
				    } else{  
					    alert("Seleccione colación.");  
                            }  
                }
            if(current==1){
                next_step = $(this).parent().next();
                    next_step.show();
                    current_step.hide();
                    setProgressBar(++current);
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