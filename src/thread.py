from collections import namedtuple
import openai
from copy import deepcopy

from .prompt_builder import PromptBuilder
from .parameters import default_gpt_parameters as gpt
from .parameters import default_system_prompt

Message = namedtuple('Message', ['role', 'content'])


def message_mapping(messages):
    return list(map(lambda m: {'role': m.role, 'content': m.content}, messages)) 

class Thread:
    
    def __init__(self, system_prompt=None):
        self.__messages = []

        system_prompt_message = Message('system', system_prompt if system_prompt else default_system_prompt)
        self.__messages.append(system_prompt_message)
    
    
    def add_user_prompt(self, prompt: str):
        self.__messages.append(Message('user', prompt))
        return self
        
        
    def send(self) -> Message:
        response = openai.ChatCompletion.create(
                engine=gpt.engine,
                model=gpt.model,
                
                messages = message_mapping(self.__messages),
                
                temperature=gpt.temperature,
                max_tokens=gpt.max_tokens,
                top_p=gpt.top_p,
                frequency_penalty=gpt.frequency_penalty,
                presence_penalty=gpt.presence_penalty,
                stop=gpt.stop)
        
        response_message = Message(response.choices[0].message.role, response.choices[0].message.content)
        self.__messages.append(response_message)
        
        return response_message
    
    
    def get_messages(self):
        return deepcopy(self.__messages)
        
    