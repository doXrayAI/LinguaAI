import persistence 
from src.bots.chatbot import StatelessChatBot

def add_new_chat(setting_description, GPT_role, user_role, language, language_level):
    
    # get initial GPT chat messages
    chat = initialize_GPT_chat(setting_description, GPT_role, user_role, language, language_level) 
    
    return persistence.persist_new_chat(language, language_level, setting_description, GPT_role, user_role, chat).to_dict('records')

    
def get_chat_messages(id):
    return persistence.load_chat_messages(id).to_dict('records')


def get_chats():
    return persistence.load_chat_ids_and_context().to_dict('records')

    
def initialize_GPT_chat(setting, GPT_role, user_role, language, language_level):
    b = StatelessChatBot()
    messages = b.init_conversation(setting, GPT_role, user_role, language, language_level, 4)
    return messages

def new_message(message, chat_id):
    b = StatelessChatBot()
    chat = persistence.load_chat_messages(chat_id)
    
    previous_messages = chat['chat'].tolist()[0]
            
    new_messages = b.send(previous_messages, message)
    
    persistence.persist_updated_chat(chat_id, new_messages)
    
    return new_messages