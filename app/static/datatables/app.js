/*

Copyright (c) 2019 - present AppSeed.us

*/

"use strict";
const doc = document;
doc.addEventListener("DOMContentLoaded", function(event) {

    // Used for API Requests 
    var xhr1 = new XMLHttpRequest();
 
    // Toasts
    const notyf = new Notyf({
        position: {
            x: 'right',
            y: 'top',
        },
        types: [
            {
                type: 'info',
                background: '#FA5252',
                icon: {
                    className: 'fas fa-comment-dots',
                    tagName: 'span',
                    color: '#fff'
                },
                dismissible: false
            }
        ]
    });

    // Used by cell edit
    document.addEventListener('keydown', event => {

        // Catch 'ENTER' event
        if (event.key === 'Enter') {
          
            // If applies on a TD  
            if (event.target.matches('td.editable')) {
          
                // Drop the default event
                event.preventDefault();
                            
                let td = event.target;
                let tr = event.target.closest('tr.editable');

                let data_id    = tr.dataset.id;            
                let data_name  = td.dataset.name;
                let data_value = td.textContent;
                
                xhr1.open("PUT", "/api/data/field/" + data_id); 
                xhr1.setRequestHeader("Content-Type", "application/json");
                
                // Check Status
                xhr1.onreadystatechange = function() {
                    
                    if (this.status == 200 && this.readyState == 4) { 

                        notyf.open({
                            type: 'success',
                            message: 'Information saved successfully'
                        });                        
                    }    
                    
                    // XMLHttpRequest returns 0 on success
                    if ( (this.status > 0) && (this.status != 200) ) { 
                        
                        notyf.open({
                            type: 'error',
                            message: 'Error!'
                        });
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
        
            let td = event.target;
            let tr = event.target.closest('tr.editable');

            let data_id   = tr.dataset.id;            
            let data_name = td.dataset.name;
                        
            // Enable 'EDITABLE' property
            td.setAttribute("contenteditable", "true");
        }

        // ROW Delete event
        if (event.target.matches('.row-delete')) {

            // Drop the default event
            event.preventDefault();
        
            let tr = event.target.closest('tr.editable');
            let data_id = tr.dataset.id;

            xhr1.open('DELETE', "/api/data/" + data_id, true);
            
            // Check Status
            xhr1.onreadystatechange = function() {
                
                if (this.status == 200 && this.readyState == 4) { 

                    tr.remove();

                    notyf.open({
                        type: 'success',
                        message: 'Information deleted successfully'
                    });     
                }    

                // XMLHttpRequest returns 0 on success
                if ( (this.status > 0) && (this.status != 200) ) { 

                    notyf.open({
                        type: 'error',
                        message: 'Error! ' + this.status
                    }); 
                }

            };//end onreadystate

            xhr1.send();

        }
    
    }, false); 

}); 
