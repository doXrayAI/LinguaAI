from prompt_builder import PromptBuilder
from single_run_thread import SingleRunThread
from utils import load_template
from bot import Bot


class CaptionBot(Bot):
    '''Bot generating a caption based on the setting and roles'''
    def __init__(self) -> None:
        super().__init__()
        self.__template = load_template('conversation_caption_generation')
        
    
    def send(self, args) -> str:
        self._prompt_builder.add_template(self.__template['template'], args)
        
        prompt = self._prompt_builder.build()
        self._prompt_builder.reset()
        
        caption = self._thread.send(prompt)
        
        return caption