from prompt_builder import PromptBuilder
from single_run_thread import SingleRunThread
from utils import load_template


class CaptionBot:
    
    def __init__(self) -> None:
        self.__prompt_builder = PromptBuilder()
        self.__thread = SingleRunThread()
        self.__template = load_template('conversation_caption_generation')
        
    
    def generate(self, setting, gpt_role, user_role ) -> str:
        self.__prompt_builder.add_template(self.__template['template'], (setting, gpt_role, user_role))
        
        prompt = self.__prompt_builder.build()
        self.__prompt_builder.reset()
        
        caption = self.__thread.send(prompt)
        
        return caption