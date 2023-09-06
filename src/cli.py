from src.bots.input_validation_bot import InputValidationBot
from src.bots.role_inference_bot import RoleInferenceBot
from src.bots.caption_bot import CaptionBot
from src.bots.chatbot import ChatBot
from src.bots.summarization_bot import SummarizationBot
from src.bots.refinement_bot import *
from src.bot_pipeline import make_bot_pipeline
from src.parameters import summarization_parametes
from src.bot_operator import ChatBotOperator

def chat_initiation(summarize= False):
        
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
    
    # Bot list and refinement pipeline with the best refinement bot alternatives    
    bot_list = [RoleFitnessBot(roles['GPT_role'], roles['user_role'], setting_description, alternative=4), LanguageLevelBot( language_level, alternative=3), LanguageLevelSimplificationBot(language_level) ]    
    pipeline = make_bot_pipeline([b.send for b in bot_list])
    
    # Initialize chat bot
    chat_bot = ChatBot(roles['setting'], roles['GPT_role'], roles['user_role'], language, language_level, init_alternative=4, chat_alternative=0 )
    
    
    # Initialize chatbot operator
    operator = ChatBotOperator(chat_bot, pipeline)
    
    chatbot_message = operator.chatbot_setup()
    print(chatbot_message)
    
    summary = ''
    summarization_bot = SummarizationBot(4, summarization_parametes)
    summary_window = 4
    
    while 1:
        m = input(roles['user_role'] + ': ')
        
        m = roles['user_role'] + ': ' + m

        gpt_response = operator.send_message(m)
        
        print(gpt_response)
        
        if summarize:
            length = operator.get_dialogue_length()
            print(length)
            if length > 0 and length % summary_window == 1:
                chat_string = operator.get_dialogue_string(summary_window)
                new_summary = summarization_bot.send(summary, chat_string)
                print('SUMMARY: ' + new_summary)
                print('SUMMARY LEN: ' + str(len(new_summary)))
                summary = new_summary
        

    
    
