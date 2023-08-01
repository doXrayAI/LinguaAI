from bot import Bot
from utils import load_template


class LanguageLevelRefinementBot(Bot):
    
    def __init__(self, language_level):
        super().__init__()
        self.__template = dict()
        self.__template = load_template('language_level_refinement_description')
        self._prompt_builder.add_template(self.__template['template'], (language_level,))
        
        
    def send(self, input) :
        
        self._prompt_builder.add_template(input)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        return refinement