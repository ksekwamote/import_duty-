

$( document ).ready(function() {

    //myFunction(x)
   
})

function custom() {

					var cSelect = document.getElementById("country")
					var country = cSelect.options[cSelect.selectedIndex].value
					var pcSelect = document.getElementById("category")
					var product = pcSelect.options[pcSelect.selectedIndex].value
					var price = document.getElementById("price").value
         
        



               if((validate(price, product, country) == -1)){

                  return;
               }








					 var sadc_countries = ['Angola', 'Botswana', 'Congo', 'Lesotho', 'Namibia', 'South Africa',
                      'Swaziland', 'Zambia', 'Zimbabwe']

                      var EU_countries = ['England', 'Italy', 'France', 'Belgium', 'Germany']
                      var category;
                     switch(product){
                     	case "Accesories (no battery)":
                     		category=1;
                     		break;
                     	case "Accesories (with battery)":
                     		category=2;
                     		break;
                     	case "Audio/Video":
                     		category=3;
                     		break;
                     	case "Bags & Luggage":
                     		category=4;
                     		break
                     	default:
                     		category=0;

                     }
                     var duty;
                     if (sadc_countries.includes(country)){
                     	switch(category){
                     		case 1:
                     			duty=0.1
                     			break;
                     		case 2:
                     			duty=0.15
                     			break;
                     		case 3:
                     			duty=0
                     			break;
                     		case 4:
                     			duty=0
                     			break
                     		default:
                     			duty=0;
                     	}
                     }
                    else{

                    	switch(category){
                     		case 1:
                     			duty=0.1
                     			break;
                     		case 2:
                     			duty=0.15
                     			break;
                     		case 3:
                     			duty=0
                     			break;
                     		case 4:
                     			duty=0.2
                     			break
                     		default:
                     			duty=0;
                     	}

                    }

                  var tax = 0.15*price
                  var import_duty = duty*price
                  var total_cost = Number(price)+ Number(tax)+ Number(import_duty)
                  var total = total_cost.toFixed(2)



               

                 if (tax > 500){

                     document.getElementById("res").innerHTML =`<div class="negative">
                <div class="callout">
                    😢 Oh no, looks like you’ll have to pay $<strong class="result-costs">`+tax.toFixed(2)+`</strong>
                    in taxes!
                </div>

                <div class="explanation">
                    Additionally, you'll be charged a duty fee of $
                    <strong class="result-duty">`+import_duty.toFixed(2)+`</strong> 
                </div>

                <div class="details">
                    Which brings your total to $
                    <strong class="result-duty">`+total+`</strong> 
                </div>
            </div>`
                 }

                 else if (tax <50){

                     document.getElementById("res").innerHTML =`<div class="negative">
                <div class="callout">
                    &#128521  Not too bad, you’ll have to pay $<strong class="result-costs">`+tax.toFixed(2)+`</strong>
                    in taxes!
                </div>

                <div class="explanation">
                    Additionally, you'll be charged a duty fee of $
                    <strong class="result-duty">`+import_duty.toFixed(2)+`</strong> 
                </div>

                <div class="details">
                    Which brings your total to $
                    <strong class="result-duty">`+total+`</strong> 
                </div>
            </div>`

                 }

                 else{  

                  document.getElementById("res").innerHTML =`<div class="negative">
                <div class="callout">
                    &#128542  Yikes! , you’ll have to pay $<strong class="result-costs">`+tax.toFixed(2)+`</strong>
                    in taxes!
                </div>

                <div class="explanation">
                    Additionally, you'll be charged a duty fee of $
                    <strong class="result-duty">`+import_duty.toFixed(2)+`</strong> 
                </div>

                <div class="details">
                    Which brings your total to $
                    <strong class="result-duty">`+total+`</strong> 
                </div>
            </div>`

                 }

                 
            

				}

				function validate(value , category, country){

					

            if (value == 0.00 && category != "-1" && country != "-1"){

                  document.getElementById("res").innerHTML =`<div class="positive">
                <div class="callout">
                  🥳 WHOOO! 0 Costs mean 0 Taxes , or you made a mistake, Try again!
                </div>

                <div class="explanation">
                    Fill Out the details again <span class="result-taxrate"></span> and 
                    <strong class="result-vat">PRESS</strong> the button below &#128071 &#128071
                </div>
            </div>

          </div>`
               return -1
            }

           if (value != 0.00 && category != "-1" && country == "-1" ){

                  document.getElementById("res").innerHTML =`<div class="positive">
                <div class="callout">
                  &#128558 SORRY! Think you made a mistake! , you forgot to select country.  
                </div>

                <div class="explanation">
                    Fill Out the details again <span class="result-taxrate"></span> and 
                    <strong class="result-vat">PRESS</strong> the button below &#128071 &#128071
                </div>
            </div>

          </div>`
               return -1
       }

      if (value != 0.00 && category == "-1" && country == "-1" ){

                  document.getElementById("res").innerHTML =`<div class="positive">
                <div class="callout">
                  &#128562 SORRY! Think you made a mistake! , you forgot to select both country and category.  
                </div>

                <div class="explanation">
                    Fill Out the details again <span class="result-taxrate"></span> and 
                    <strong class="result-vat">PRESS</strong> the button below &#128071 &#128071
                </div>
            </div>

          </div>`
               return -1
       }


       if (value == 0.00 && category == "-1" && country == "-1"){

                  document.getElementById("res").innerHTML =`<div class="positive">
                <div class="callout">
                  &#128556 You barely touched anything
                </div>

                <div class="explanation">
                    Fill Out the details again <span class="result-taxrate"></span> and 
                    <strong class="result-vat">PRESS</strong> the button below &#128071 &#128071
                </div>
            </div>

          </div>`
               return -1
            }

       if(country == "-1"){


         document.getElementById("res").innerHTML =`<div class="positive">
                <div class="callout">
                  &#128558 SORRY! Think you made a mistake! , you forgot to select country.  
                </div>

                <div class="explanation">
                    Fill Out the details again <span class="result-taxrate"></span> and 
                    <strong class="result-vat">PRESS</strong> the button below &#128071 &#128071
                </div>
            </div>

          </div>`
               return -1



       }   



       if(category == "-1"){


         document.getElementById("res").innerHTML =`<div class="positive">
                <div class="callout">
                  &#128556 OOOPS! Think you made a mistake! , you forgot to select category.  
                </div>

                <div class="explanation">
                    Fill Out the details again <span class="result-taxrate"></span> and 
                    <strong class="result-vat">PRESS</strong> the button below &#128071 &#128071
                </div>
            </div>

          </div>`
               return -1



       } 




				}