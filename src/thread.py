from collections import namedtuple
import openai
from copy import deepcopy

from prompt_builder import PromptBuilder
from parameters import default_parameters
from parameters import default_system_prompt






class Thread:
    '''Class encapsulating API call to GPT. Sends multiple assistant and user messages from the same conversation thread'''
    
    def __init__(self, system_prompt=default_system_prompt, params=default_parameters):
        '''Initializes message list with system_prompt, stores parameters for ChatCompletion API call'''
        self.__messages = []
        self.__params = params

        system_prompt_message = {'role': 'system', 'content': system_prompt}
        self.__messages.append(system_prompt_message)
    
    
    def add_user_prompt(self, prompt: str):
        '''Adding user prompt to the message list.'''
        self.__messages.append({'role':'user', 'content': prompt})
        return self
    
    
    def add_assistant_prompt(self, prompt: str):
        '''Adding user prompt to the message list.'''
        self.__messages.append({'role':'assistant', 'content': prompt})
        return self
    
        
    def send(self) -> dict:
        '''Calls GPT API with stored messages. Returns the API response.'''
        
        response = openai.ChatCompletion.create(
                model=self.__params.model,
                messages = self.__messages,
                temperature=self.__params.temperature,
                max_tokens=self.__params.max_tokens,
                top_p=self.__params.top_p,
                frequency_penalty=self.__params.frequency_penalty,
                presence_penalty=self.__params.presence_penalty,
                stop=self.__params.stop)
        
        response_message = {'role': response.choices[0].message.role, 'content': response.choices[0].message.content}
        return response_message
    
    
    def get_messages(self):
        return deepcopy(self.__messages)
    
    
    def pop(self):
        '''Removes and returns the last added message from the list.'''
        if len(self.__messages) > 0:
            return self.__messages.pop()

        return None