from bot import Bot
from thread import Thread
from utils import load_template, load_cefr
from src.single_run_thread import StatelessThread
from src.parameters import default_system_prompt
from src.templates.alternatives.chatbot_initiation import chatbot_initiation_alternatives

class ChatBot(Bot):
    '''A generic chatbot'''
    
    def __init__(self, setting_description, GPT_role, user_role, language='English', language_level='A1', init_alternative=1) -> None:
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
    
    
    
class StatelessChatBot(Bot):
    
    def __init__(self):
        super().__init__(thread=StatelessThread() )
        
    
    def init_conversation(self, setting_description, GPT_role, user_role, language='English', language_level='A1', init_alternative=1):
        
        template = chatbot_initiation_alternatives[init_alternative]
        level_description = load_cefr(language_level)
        
        args = (setting_description, language, user_role, GPT_role, language_level, level_description)
        prompt = self._prompt_builder.add_template(template, args).build()
        messages = [ {'role': 'system', 'content': default_system_prompt}, { 'role': 'user', 'content' : prompt},]
        messages.append( self._thread.send(messages))
        return messages
        
    def send(self, messages, new_message):
        messages = deepcopy(messages)
        messages.append({'role': 'user', 'content': new_message})
        response = self._thread.send(messages)
        messages.append(response)
        
        return messages
        
        
        
        
        
    