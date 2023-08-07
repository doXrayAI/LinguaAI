from src.bots.input_validation_bot import InputValidationBot
from src.bots.role_inference_bot import RoleInferenceBot
from src.bots.caption_bot import CaptionBot
from src.bots.chatbot import ChatBot
from src.bots.refinement_bot import *
from src.bot_pipeline import make_bot_pipeline
from src.bot_operator import ChatBotOperator

def chat_initiation():
        
    validation_bot = InputValidationBot()
    role_inference_bot = RoleInferenceBot()
    
    valid_input = False
    
    language = input('Language ').strip()
    language_level = input('Language level (i.e. A1): ').strip()
    
    while language_level not in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        language_level = input('Language level: ').strip()
    
    
    setting_description = None
    while not valid_input:
        setting_description =  input('Setting description: ')
        
        valid_input = validation_bot.send((setting_description,))
        
        if not valid_input:
            print('Invalid input')
        
    roles = role_inference_bot.send((setting_description,))
    
    print(roles)
        
    caption_bot = CaptionBot()
    caption = caption_bot.send((setting_description, roles['GPT_role'], roles['user_role']))
    
    print(caption)
    
    
    #bot_list = [RoleFollowingBot(roles['GPT_role'], roles['user_role']), UserEngagementBot(roles['GPT_role'], roles['user_role'], roles['setting']), LanguageLevelRefinementBot(language_level) ]    
    
    bot_list = [RoleFollowingBot(roles['GPT_role'], roles['user_role']), LanguageLevelRefinementBot(language_level) ]    
    pipeline = make_bot_pipeline([b.send for b in bot_list])
    
    # Initialize chat bot
    chat_bot = ChatBot(roles['setting'], roles['GPT_role'], roles['user_role'], language, language_level)
    
    
    # Initialize chatbot operator
    
    operator = ChatBotOperator(chat_bot, pipeline)
    
    chatbot_message = operator.chatbot_setup()
    print(chatbot_message)
    
    while 1:
        m = input(roles['user_role'] + ': ')
        
        m = roles['user_role'] + ': ' + m

        gpt_response = operator.send_message(m)
        
        print(gpt_response)
    
    
    
