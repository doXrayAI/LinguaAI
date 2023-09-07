

export function get_chats(){
    
    let url = `/chats`

    fetch(url)
        .then((response) => response.json())
        .then((data)=> {
            console.log(data)
        })
        .catch((error) => {
            console.error("Error fetching chats: ", error)
        })
}


export function get_chat_messages(id){
    let url = `/chat_messages/${id}`

    fetch(url)
        .then((response) => response.json())
        .then((data)=>{
            console.log(data)
        })
        .catch((error) => {
            console.error(`Error fetching messages for id ${id}: `, error)
        })
}



export function validate_context(user_language, language_level, setting_description){
    let url = `/context/${user_language}/${language_level}/${setting_description}`

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            console.log(data.content)
        })
}


export function infer_roles(setting) {
    let url = `/roles/${setting}`

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
        })
        .catch((error) => {
            console.error("Error getting roles:", error)
        })
}

