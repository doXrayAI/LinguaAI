from input_validation_bot import InputValidationBot
from role_inference_bot import RoleInferenceBot
from caption_bot import CaptionBot

def chat_initiation():
        
    validation_bot = InputValidationBot()
    role_inference_bot = RoleInferenceBot()
    
    valid_input = False
    
    setting_description = None
    while not valid_input:
        setting_description =  input('Setting description: ')
        
        valid_input = validation_bot.validate(setting_description)
        
        if not valid_input:
            print('Invalid input')
        
    roles = role_inference_bot.infere(setting_description)
    
    print(roles)
        
    # TODO generate setting caption
    caption_bot = CaptionBot()
    caption = caption_bot.generate(setting_description, roles['GPT_role'], roles['user_role'])
    
    print(caption)
    
    # TODO create bot pipeline, add chat thread and auxiliary threads to it
    
    # TODO conversation
    
    
