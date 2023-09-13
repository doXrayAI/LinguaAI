import persistence 
from src.bots.chatbot import StatelessChatBot
from src.bots.refinement_bot import *
from src.bot_pipeline import make_bot_pipeline



def add_new_chat(setting_description, GPT_role, user_role, language, language_level):
    chat = initialize_GPT_chat(setting_description, GPT_role, user_role, language, language_level) 
    return persistence.persist_new_chat(language, language_level, setting_description, GPT_role, user_role, chat).to_dict('records')[0]

    
def get_chat_messages(id):
    return persistence.load_chat_messages(id).to_dict('records')[0]


def get_chats():
    return persistence.load_chat_ids_and_context().to_dict('records')

    
def initialize_GPT_chat(setting, GPT_role, user_role, language, language_level):
    bot = StatelessChatBot()
    messages, initial_response = bot.init_conversation(setting, GPT_role, user_role, language, language_level, 4)
    
    bot_list = [RoleFitnessBot(GPT_role, user_role, setting, alternative=4), LanguageLevelBot(language_level, alternative=3), LanguageLevelSimplificationBot(language_level) ]    
    pipeline = make_bot_pipeline([b.send for b in bot_list])
    
    refined_initial_response, _ = pipeline(initial_response, [])
    messages.append({'role': 'assistant', 'content': refined_initial_response})
    return messages

def new_message(message, chat_id):
    bot = StatelessChatBot()
    chat = persistence.load_chat_messages(chat_id).to_dict('records')[0]
    messages = chat['chat']
    messages.append({'role': 'user', 'content': message})

    roles = chat['role_object']
            
    response = bot.send(messages)
    bot_list = [RoleFitnessBot(roles['GPT_role'], roles['user_role'], roles['setting'], alternative=4), LanguageLevelBot(chat['language_level'], alternative=3), LanguageLevelSimplificationBot(chat['language_level']) ]    
    pipeline = make_bot_pipeline([b.send for b in bot_list])
        
    refined_response, _ = pipeline(response, [])
    messages.append({'role': 'assistant', 'content': refined_response})
    
    return persistence.persist_updated_chat(chat_id, messages).to_dict('records')[0]

    
    