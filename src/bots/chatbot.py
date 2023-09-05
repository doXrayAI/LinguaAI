from bot import Bot
from thread import Thread
from utils import load_template, load_cefr
from src.templates.alternatives.chatbot_initiation import chatbot_initiation_alternatives

class ChatBot(Bot):
    '''A generic chatbot'''
    
    def __init__(self, setting_description, GPT_role, user_role, language='English', language_level='A1', init_alternative=1, chat_alternative=0) -> None:
        super().__init__(thread=Thread())
        
        template = chatbot_initiation_alternatives[init_alternative]
        level_description = load_cefr(language_level)
        
        args = (setting_description, language, user_role, GPT_role, language_level, level_description)
        prompt = self._prompt_builder.add_template(template, args).build()
        self._prompt_builder.reset()
        
        self._thread.add_user_prompt(prompt)
        
        
    def send(self):
        return self._thread.send()
        
        
    def add_message(self, message, role= 'user'):
        '''Adds message into the thread'''
        if role == 'user':
            self._thread.add_user_prompt(message)
        else:
            self._thread.add_assistant_prompt(message)
            
            
    def get_chat(self):
        return self._thread.get_messages()
    

    def get_dialogue_length(self):
        return self._thread.get_dialogue_length()
    
    
    def get_dialogue_string(self, window=6):
        return self._thread.get_dialogue_string(window)