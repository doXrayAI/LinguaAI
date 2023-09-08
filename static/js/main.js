import {show_hide_invalid_setting_message, show_roles } from './validation.js'
import {get_chat_messages, get_chats, infer_roles, validate_context, create_new_chat} from './api_call.js'
import { render_previous_chats } from './chat_list.js';

let chats = [];

// Event listener on submit
window.onload = function () {
    show_hide_invalid_setting_message(true);

    $("#user-selection-form").on("submit", async function (event){
      event.preventDefault();

      // Get user inputs
      let user_language = $("#language").val();
      let language_level = $("#language-level").val();
      let setting_description = $("#setting-description").val();

      let c = await validate_context(user_language, language_level, setting_description)
        .then((valid)=> {
            if(valid){
              return infer_roles(setting_description)
            }
            else{
              show_hide_invalid_setting_message(valid)
              return Promise.reject(new Error('Invalid context'))
            }
        })
        .then((r) => {
           console.log('Creating a chat')
           return create_new_chat(setting_description, r.GPT_role, r.user_role, user_language, language_level)
        })
        .catch((error) => {
          console.error('Error in new chat description: ', error)
        })
        

      console.log('WE HAVE A CHAT:')
      console.log(c)

    });
};

// Load previous chats and render them
$(async function(){

  chats = await get_chats()

  // store fetched chats to session storage
  sessionStorage.setItem("chats", chats)

  // store selected chat to session storage

  selected_chat_idx = -1
  if(chats.length > 0)
    selected_chat_idx = -1
  sessionStorage.setItem("selected_chat_idx", selected_chat_idx)

  render_previous_chats(chats)

  // TODO: event listeners on chats -> click -> fetch messages and render them on the right
  // If selected chat (session storage) is different from -1, fetch and render the messages on the right
})




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

