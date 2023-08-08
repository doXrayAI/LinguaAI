from bot import Bot
from thread import Thread
from utils import load_template, load_cefr

class ChatBot(Bot):
    '''A generic chatbot'''
    
    def __init__(self, setting_description, GPT_role, user_role, language='english', language_level='A1') -> None:
        super().__init__(thread=Thread())
        
        template = load_template('chat_bot_initiation')
        level_description = load_cefr(language_level)
        
        args = (setting_description, language, user_role, GPT_role, language_level, level_description)
        prompt = self._prompt_builder.add_template(template['template'], args).build()
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