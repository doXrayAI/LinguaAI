

export function show_hide_invalid_setting_message(valid){

    $("#description-error").text("");

    if (!valid) {
        // Display an error message in red
        $("#description-error").text("Setting description is not valid. Please try something else.");
        // clear the input
        $("#setting-description").val("")
    }

}

export function show_roles(role_object){

    $("#roles").textContent = `Bot takes the role of ${role_object.GPT_role}. Your role is ${role_object.user_role}.`
    $("#setting").textContent = `The setting of your conversation is: ${role_object.setting}`
}



// renders previous chats and adds event listeners on click
export function render_previous_chats(chats, listener_function){

    let element = $("#previous-chat-container")

    let chat_string = ""

    chats.forEach(e => {
        chat_string += `<div class="row sideBar-body chat-sidebar" data-chatid=${e.id}>
        <div class="col-sm-3 col-xs-3 sideBar-avatar">
          <div class="avatar-icon">
            <img src="https://bootdey.com/img/Content/avatar/avatar1.png">
          </div>
        </div>
        <div class="col-sm-9 col-xs-9 sideBar-main">
          <div class="row">
            <div class="col-sm-8 col-xs-8 sideBar-name" style="height:100px">
              <span class="name-meta">${e.role_object.GPT_role[0].toUpperCase() + e.role_object.GPT_role.slice(1)}
            </span><br>
              <span class="time-meta">${e.role_object.setting}
              </span> <br>
            </div>
            <div class="col-sm-4 col-xs-4 pull-right sideBar-time">
              <span class="time-meta pull-right">${e.language} ${e.language_level}
              </span>
            </div>
          </div>
        </div>
      </div>`
    });
    
    element.prepend(chat_string)

    // Add listeners on click 
    $(".chat-sidebar").on("click", listener_function)
}



export function render_current_chat(chat){

    let id = sessionStorage.getItem("selected_chat_id")
    let conversation = $("#conversation")

    if(id != undefined && id > -1)
    {
        // Set heading name
        let heading_name = $(".heading-name-meta")
        heading_name.html(chat.role_object.GPT_role[0].toUpperCase() + chat.role_object.GPT_role.slice(1))


        // Set messages content
        let messages = chat.chat
        let messages_string = ""

        messages.slice(2).forEach(m => {

            let role_class = 'receiver'
            if(m.role=='user')
                role_class = 'sender'   

            messages_string +=
                `<div class="row message-body">
                <div class="col-sm-12 message-main-${role_class}">
                  <div class="${role_class}">
                    <div class="message-text">
                     ${m.content[0].toUpperCase() + m.content.slice(1)}
                     </span><br>
                    </div>
                  </div>
                </div>
              </div>
                `
        });

        conversation.html(messages_string)
    }
    else{
        conversation.html('')
    }

    conversation.scrollTop(conversation.prop("scrollHeight"));
}





