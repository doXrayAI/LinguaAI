

export function render_current_chat(chat){


    let id = sessionStorage.getItem("selected_chat_id")

    console.log("ID: ", id)
    
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
                     ${m.content}
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

}



