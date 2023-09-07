

function pr(){

    console.log("KKKKKKKKK")

}

function show_hide_invalid_setting_message(valid = True){

    document.getElementById("description-error").textContent = "";

    if (!valid) {
        // Display an error message in red
        document.getElementById("description-error").textContent = "Setting description is not valid. Please try something else.";
        // clear the input
        document.getElementById("setting-description").value = ""
    }

}

function show_roles(role_object){

    document.getElementById("roles").textContent = `Bot takes the role of ${role_object.GPT_role}. Your role is ${role_object.user_role}.`
    document.getElementById("setting").textContent = `The setting of your conversation is: ${role_object.setting}`
}


export {pr, show_hide_invalid_setting_message, show_roles}