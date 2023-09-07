import {pr, show_hide_invalid_setting_message, show_roles } from './validation.js'


let language_global;
let language_level_global;
let role_object_global;



window.onload = function () {
    show_hide_invalid_setting_message(true);

    document
    .getElementById("user-selection-form")
    .addEventListener("submit", function (event) {
      // Prevent the form from submitting and refreshing the page
      event.preventDefault();

      let user_language = document.getElementById("language").value;
      let language_level = document.getElementById("language-level").value;
      let setting_description = document.getElementById("setting-description").value;

      let url = `/context/${user_language}/${language_level}/${setting_description}`

      console.log(url)

      language_global = user_language
      language_level_global = language_level

      fetch(url)
        .then((response) => response.json())
        .then((data) => {
            let valid_state = data.content
            console.log(valid_state)

            show_hide_invalid_setting_message(valid_state)

            if(valid_state){
                console.log(user_language)

                let url_roles = `/roles/${setting_description}`

                fetch(url_roles)
                    .then((response) => response.json())
                    .then((data) => {
                        let roles = data.content
                        console.log(roles)

                        //show_roles(roles)
                        
                        role_object_global = roles

                    })
                .catch((error) => {
                    console.error("Error getting roles:", error)
                })
            }
        })
        .catch((error) => {
            console.error("Error fetching context response:", error);
          });
    });

};


$(function(){
    $(".heading-compose").click(function() {
      $(".side-two").css({
        "left": "0"
      });
    });

    $(".newMessage-back").click(function() {
      $(".side-two").css({
        "left": "-100%"
      });
    });
}) 