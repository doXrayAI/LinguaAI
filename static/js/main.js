import {show_hide_invalid_setting_message, show_roles } from './validation.js'
import {get_chat_messages, get_chats, infer_roles, validate_context, create_new_chat} from './api_call.js'
import { render_previous_chats } from './chat_list.js';
import { render_current_chat } from './current_chat.js';

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
           console.log(r)
           return create_new_chat(setting_description, r.GPT_role, r.user_role, user_language, language_level)
        })
        .catch((error) => {
          console.error('Error in new chat description: ', error)
        })
        

      console.log('WE HAVE A CHAT:')
      console.log(c)

      // TODO: add chat to the chat list from session storage
      let chats = JSON.parse(sessionStorage.getItem("chats"))
      console.log('Chats:', chats)
      chats.unshift(c)
      sessionStorage.setItem("chats", JSON.stringify(chats))

      // TODO: make it the selected chat
      sessionStorage.setItem("selected_chat_id", c.id)

      // TODO: rerender the chat list
      render_previous_chats(chats)

      // TODO: rerender the message panel

      // TODO: close side-two panel
      $(".side-two").css({
        "left": "0"
      });

    });
};

// Load previous chats and render them
$(async function(){

  let chats = await get_chats()

  // store fetched chats to session storage
  sessionStorage.setItem("chats", JSON.stringify(chats))

  // store selected chat to session storage

  let selected_chat_id = -1
  if(chats.length > 0)
    selected_chat_id = chats[0].id
  sessionStorage.setItem("selected_chat_id", selected_chat_id)

  render_previous_chats(chats)

  // TODO: event listeners on chats -> click -> fetch messages and render them on the right
  // If selected chat (session storage) is different from -1, fetch and render the messages on the right

  if(selected_chat_id != -1){
    let chat = await get_current_chat_messages()

    console.log('Chat',chat)

    render_current_chat(chat)
  }
  
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



async function get_current_chat_messages(){

  let id = sessionStorage.getItem("selected_chat_id")
  
  if(id != undefined && id > -1)
  {
      let chat = await get_chat_messages(id)

      return chat
  }

  return undefined

}