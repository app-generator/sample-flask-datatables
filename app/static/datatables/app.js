/*

Copyright (c) 2019 - present AppSeed.us

*/

"use strict";
const doc = document;
doc.addEventListener("DOMContentLoaded", function(event) {

    var xhr1 = new XMLHttpRequest();
 
    document.addEventListener('keydown', event => {

        // Catch 'ENTER' event
        if (event.key === 'Enter') {
          
            // If applies on a TD  
            if (event.target.matches('td.editable')) {
          
                // Drop the default event
                event.preventDefault();
            
                // Log the clicked element in the console
                // console.log(event.target);
                console.log( 'EVENT -> Cell Save' );
                
                let td = event.target;
                let tr = event.target.closest('tr.editable');

                let data_id    = tr.dataset.id;            
                let data_name  = td.dataset.name;
                let data_value = td.textContent;
                
                console.log( ' >> Save Data [' + data_id  + '] ' + data_name + ' = [' + data_value + ']' );
                
                xhr1.open("PUT", "/api/data/field/" + data_id); 
                xhr1.setRequestHeader("Content-Type", "application/json");
                
                // Check Status
                xhr1.onreadystatechange = function() {
                    
                    if (this.status == 200 && this.readyState == 4) { 
                        console.log( ' >>> Editing OK' ); 
                    }    
                    
                    if (this.status != 200) { 
                        console.log( ' >>> Editing ERR ' + this.status ); 
                    }

                };//end onreadystate

                xhr1.send(JSON.stringify( { data_name: data_name, data_value: data_value } ));

                // Disable 'EDITABLE' property    
                td.setAttribute("contenteditable", "false");

            } // END if (event.target.matches('td.editable')) {

        } // END if (event.key === 'Enter') { 

      });

    // handle Clicks     
    document.addEventListener('click', function (event) {

        // Cell Edit event
        if (event.target.matches('td.editable')) {

            // Drop the default event
            event.preventDefault();
        
            // Log the clicked element in the console
            // console.log(event.target);
            console.log( 'EVENT -> Cell Edit' );
            
            let td = event.target;
            let tr = event.target.closest('tr.editable');

            let data_id   = tr.dataset.id;            
            let data_name = td.dataset.name;
            
            console.log( ' >> Edit Data ' + data_id  + ' -> ' + data_name );
            
            // Enable 'EDITABLE' property
            td.setAttribute("contenteditable", "true");
        }

        // ROW Delete event
        if (event.target.matches('.row-delete')) {

            // Drop the default event
            event.preventDefault();
        
            // console.log(event.target);
            console.log( 'EVENT -> ROW Delete' );

            let tr = event.target.closest('tr.editable');
            let data_id = tr.dataset.id;

            console.log( ' >>> DELETE ID = ' + data_id ); 

            xhr1.open('DELETE', "/api/data/" + data_id, true);
            
            // Check Status
            xhr1.onreadystatechange = function() {
                
                if (this.status == 200 && this.readyState == 4) { 
                    console.log( ' >>> Deletion OK' ); 
                    tr.remove();
                }    
                
                if (this.status != 200) { 
                    console.log( ' >>> Deletion ERR ' + this.status ); 
                }

            };//end onreadystate

            xhr1.send();

        }
    
    }, false); 

}); 
