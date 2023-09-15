from src.bots.bot import Bot
from src.parameters import default_parameters
from src.bots.chatbot import ChatBot
from src.single_run_thread import SingleRunThread
from src.templates.alternatives.summarization import summarization_prompt_templates

class SummarizationBot(Bot):
    '''Bot producing a summary based on a previous summary 
    and a string concatenation of new messages from '''
    
    def __init__(self, prompt_alternative=0, parameters=default_parameters):
        super().__init__()
        
        self.__template = summarization_prompt_templates[prompt_alternative]
        self.__parameters = parameters
                
    def send(self, previous_summary, message_string) -> str:
                
        self._prompt_builder.reset()    
        self._prompt_builder.add_template(self.__template, (previous_summary, message_string))
        prompt = self._prompt_builder.build()

        summary = self._thread.send(prompt, self.__parameters)
        return summary
