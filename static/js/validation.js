

function show_hide_invalid_setting_message(valid){

    $("#description-error").text("");

    if (!valid) {
        // Display an error message in red
        $("#description-error").text("Setting description is not valid. Please try something else.");
        // clear the input
        $("#setting-description").val("")
    }

}

function show_roles(role_object){

    $("#roles").textContent = `Bot takes the role of ${role_object.GPT_role}. Your role is ${role_object.user_role}.`
    $("#setting").textContent = `The setting of your conversation is: ${role_object.setting}`
}


export {show_hide_invalid_setting_message, show_roles}