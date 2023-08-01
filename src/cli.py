from src.bots.input_validation_bot import InputValidationBot
from src.bots.role_inference_bot import RoleInferenceBot
from src.bots.caption_bot import CaptionBot
from src.bots.refinement_bot import *

def chat_initiation():
        
    validation_bot = InputValidationBot()
    role_inference_bot = RoleInferenceBot()
    
    valid_input = False
    
    setting_description = None
    while not valid_input:
        setting_description =  input('Setting description: ')
        
        valid_input = validation_bot.send((setting_description,))
        
        if not valid_input:
            print('Invalid input')
        
    roles = role_inference_bot.send((setting_description,))
    
    print(roles)
        
    # TODO generate setting caption
    caption_bot = CaptionBot()
    caption = caption_bot.send((setting_description, roles['GPT_role'], roles['user_role']))
    
    print(caption)
    
    
    
    # TODO create bot pipeline, add chat thread and auxiliary threads to it
    bot_list = [RoleFollowingBot(roles['GPT_role'], roles['user_role']), LanguageLevelRefinementBot('A2'), UserEngagementBot(roles['GPT_role'], roles['user_role'], roles['setting']) ]
    
    
    
    
    # TODO conversation bot
    
    
