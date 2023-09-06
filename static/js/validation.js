

function pr(){

    console.log("KKKKKKKKK")

}

function show_hide_invalid_setting_message(valid = True){

    document.getElementById("error-message").textContent = "";

    if (!valid) {
        // Display an error message in red
        document.getElementById("error-message").textContent = "Setting Description is not valid. Please try something else.";
        // clear the input
        document.getElementById("setting-description").value = ""
    }

}

function show_roles(role_object){

    let elem = document.getElementById("roles")
    elem.textContent = `Bot takes the role of ${role_object.GPT_role}. Your role is ${role_object.user_role}.`
}


export {pr, show_hide_invalid_setting_message, show_roles}