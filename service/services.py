import persistence 
from src.bots.chatbot import ChatBot

def add_new_chat(setting_description, GPT_role, user_role, language, language_level):
    id = 111
    chat = [] # TODO get initial GPT chat messages
    
    return persistence.persist_new_chat(id, language, language_level, setting_description, GPT_role, user_role, chat)

    
def get_chat_messages(id):
    return persistence.load_chat_messages(id)


def get_chats():
    return persistence.load_chat_ids_and_context()[::-1]

    
def initialize_GPT_chat(setting, GPT_role, user_role, language, language_level):
    b = ChatBot(setting, GPT_role, user_role, language, language_level, init_alternative=4)
    messages = b.get_chat()
    print(messages)
    return messages