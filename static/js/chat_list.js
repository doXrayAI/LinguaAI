


export function render_previous_chats(chats){

    let element = $("#previous-chat-container")

    let chat_string = ""

    chats.forEach(e => {
        chat_string += `<div class="row sideBar-body">
        <div class="col-sm-3 col-xs-3 sideBar-avatar">
          <div class="avatar-icon">
            <img src="https://bootdey.com/img/Content/avatar/avatar1.png">
          </div>
        </div>
        <div class="col-sm-9 col-xs-9 sideBar-main">
          <div class="row">
            <div class="col-sm-8 col-xs-8 sideBar-name">
              <span class="name-meta">${e.role_object.GPT_role[0].toUpperCase() + e.role_object.GPT_role.slice(1)}
            </span>
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
    console.log("Running render")
}