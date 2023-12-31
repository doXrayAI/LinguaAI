export async function get_chats(){
    
    let url = `/chats`

    return fetch(url)
        .then((response) => response.json())
        .then((data)=> data)
        .catch((error) => {
            console.error(`Error fetching chats: `, error)
        })
}


export async function get_chat_messages(id){
    let url = `/chat_messages/${encodeURIComponent(id)}`

    return fetch(url)
        .then((response) => response.json())
        .then((data)=>{
            return data
        })
        .catch((error) => {
            console.error(`Error fetching messages for id ${id}: `, error)
        })
}



export async function validate_context(user_language, language_level, setting_description){
    let url = `/context/${encodeURIComponent(user_language)}/${encodeURIComponent(language_level)}/${encodeURIComponent(setting_description)}`

    return fetch(url)
        .then((response) => response.json())
        .then((data) => {
            return data.content
        })
}


export async function infer_roles(setting) {
    let url = `/roles/${encodeURIComponent(setting)}`

    return fetch(url)
        .then((response) => response.json())
        .then((data) => {
            return data
        })
}

export async function create_new_chat(setting, GPT_role, user_role, language, language_level){
    let url = `/new_chat/${encodeURIComponent(setting)}/${encodeURIComponent(GPT_role)}/${encodeURIComponent(user_role)}/${encodeURIComponent(language)}/${encodeURIComponent(language_level)}`

    return fetch(url)
        .then((response) => response.json())
        .then((data) => {
            return data
        })

}


export async function send_new_message(message, id){
    let url = `/new_message/${encodeURIComponent(message)}/${encodeURIComponent(id)}`

    return fetch(url)
        .then((response) => response.json())
}