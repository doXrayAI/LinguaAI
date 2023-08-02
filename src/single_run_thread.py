import openai

from prompt_builder import PromptBuilder
from parameters import default_parameters



class SingleRunThread:
    '''Class encapsulating API call to GPT. Can define multiple assistant and user messages.'''
    
    def send(self, prompt: str, params=default_parameters) -> str:
        '''Sends a sigle prompt to GPT API. Returns API response'''
        
        response = openai.ChatCompletion.create(
                model=params.model,
                messages = [ { 'role': 'user', 'content' : prompt},],
                temperature=params.temperature,
                max_tokens=params.max_tokens,
                top_p=params.top_p,
                frequency_penalty=params.frequency_penalty,
                presence_penalty=params.presence_penalty,
                stop=params.stop)
        
        return response.choices[0].message.content