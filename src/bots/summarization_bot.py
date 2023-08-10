from src.bots.bot import Bot
from src.bots.chatbot import ChatBot
from src.templates.alternatives.summarization import summarization_prompt_templates

class SummarizationBot(Bot):
    
    def __init__(self, prompt_alternative=0):
        super().__init__()
        
        self.__template = summarization_prompt_templates[prompt_alternative]
                
    def send(self, previous_summary, message_list) -> str:
        
        message_string = '\n'.join(message_list)
        
        self._prompt_builder.reset()    
        self._prompt_builder.add_template(self.__template, (previous_summary, message_string))
        prompt = self._prompt_builder.build()

        summary = self._thread.send(prompt)
        return summary
