import re

from src.prompt_builder import PromptBuilder
from src.single_run_thread import SingleRunThread
from src.templates.alternatives.evaluation_prompts import role_fitness_prompts, language_level_prompts
from src.utils import load_cefr

class RoleFitnessEvaluationBot:
    
    def __init__(self, prompt_alternative=0):
        self.__prompt_builder = PromptBuilder()
        self.__thread = SingleRunThread()
        self.__template = role_fitness_prompts[prompt_alternative]
        
    def evaluate(self, role, setting, dialogue_string, next_message) -> int:
        self.__prompt_builder.reset()
        self.__prompt_builder.add_template(self.__template, (role, setting, dialogue_string, next_message))
        prompt = self.__prompt_builder.build()
        
        result = self.__thread.send(prompt)
        rating = re.search(r'\d+', result).group()
        
        return int(rating)
        
    
class LanguageLevelEvaluationBot:
    
    def __init__(self, prompt_alternative=0, level_description_fname='../../templates/language_levels_cefr.json'):
        self.__prompt_builder = PromptBuilder()
        self.__thread = SingleRunThread()
        self.__template = language_level_prompts[0]
        self.__level_description_fname = level_description_fname
        
    def evaluate(self, language, language_level, message):
        
        level_description = load_cefr(language_level, self.__level_description_fname)
        
        self.__prompt_builder.reset()
        self.__prompt_builder.add_template(self.__template, (language, language_level, level_description, message))
        prompt = self.__prompt_builder.build()
        
        result = self.__thread.send(prompt)
        rating = re.search(r'\d+', result).group()
        
        return int(rating)