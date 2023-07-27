import openai

from prompt_builder import PromptBuilder
from parameters import default_completion_parameters



class CompletionThread:
    
    def send(self, prompt: str, params=default_completion_parameters) -> str:
        response = openai.Completion.create(
                model=params.model,
                
                prompt = prompt,
                
                temperature=params.temperature,
                max_tokens=params.max_tokens,
                top_p=params.top_p,
                frequency_penalty=params.frequency_penalty,
                presence_penalty=params.presence_penalty,
                stop=params.stop)
        
        return response.choices[0].text.strip()