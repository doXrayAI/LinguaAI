import {show_hide_invalid_setting_message, show_roles } from './validation.js'
import {get_chat_messages, get_chats, infer_roles, validate_context, create_new_chat, send_new_message} from './api_call.js'
import { render_previous_chats } from './chat_list.js';
import { render_current_chat } from './current_chat.js';


export async function chat_click_listener(){
  let id = $(this).attr("data-chatid")
  sessionStorage.setItem("selected_chat_id", id)
  let chat = await get_chat_messages(id)

  render_current_chat(chat)
}


export async function send_message(){

  let message_content = $("#comment").val().trim()

  if(message_content == '')
      return

  let id = sessionStorage.getItem("selected_chat_id")

  // send message to api
  let chat = await send_new_message(message_content, id)
  // render chat
  render_current_chat(chat)

  // TODO scroll to the bottom

  // clear the message from input
  $("#comment").val("")

}

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
           return create_new_chat(setting_description, r.GPT_role, r.user_role, user_language, language_level)
        })
        .catch((error) => {
          console.error('Error in new chat description: ', error)
        })
        

      // TODO: add chat to the chat list from session storage
      let chats = JSON.parse(sessionStorage.getItem("chats"))
      chats.push(c)
      sessionStorage.setItem("chats", JSON.stringify(chats))

      // make it the selected chat
      sessionStorage.setItem("selected_chat_id", c.id)

      // render the chat on top of the chat list
      render_previous_chats([c], chat_click_listener)

      // rerender the message panel
      render_current_chat(c)

      // close side-two panel by dispatching an event
      $(".newMessage-back").trigger("click")

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
    selected_chat_id = chats[chats.length-1].id
  sessionStorage.setItem("selected_chat_id", selected_chat_id)

  
  render_previous_chats(chats.reverse(), chat_click_listener)

  // If selected chat (session storage) is different from -1, fetch and render the messages on the right
  if(selected_chat_id != -1){
    let chat = await get_current_chat_messages()

    render_current_chat(chat)
  }
  
})


// add listener on message send button
$(function(){
  $("#reply-send").click(send_message);
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