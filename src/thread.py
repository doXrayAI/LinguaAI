from collections import namedtuple
import openai
from copy import deepcopy

from prompt_builder import PromptBuilder
from parameters import default_chat_completion_parameters
from parameters import default_system_prompt

Message = namedtuple('Message', ['role', 'content'])


def message_mapping(messages):
    return list(map(lambda m: {'role': m.role, 'content': m.content}, messages)) 

class Thread:
    
    def __init__(self, system_prompt=None, params=default_chat_completion_parameters):
        self.__messages = []
        self.__params = params

        system_prompt_message = Message('system', system_prompt if system_prompt else default_system_prompt)
        self.__messages.append(system_prompt_message)
    
    
    def add_user_prompt(self, prompt: str):
        self.__messages.append(Message('user', prompt))
        return self
    
    
    def add_assistant_prompt(self, prompt: str):
        self.__messages.append(Message('assistant', prompt))
        return self
    
        
    def send(self) -> Message:
        response = openai.ChatCompletion.create(
                model=self.__params.model,
                
                messages = message_mapping(self.__messages),
                
                temperature=self.__params.temperature,
                max_tokens=self.__params.max_tokens,
                top_p=self.__params.top_p,
                frequency_penalty=self.__params.frequency_penalty,
                presence_penalty=self.__params.presence_penalty,
                stop=self.__params.stop)
        
        response_message = Message(response.choices[0].message.role, response.choices[0].message.content)
        return response_message
    
    
    def get_messages(self):
        return deepcopy(self.__messages)
    
    def pop(self):
        return self.__messages.pop()
    