import re

from src.prompt_builder import PromptBuilder
from src.single_run_thread import SingleRunThread
from src.templates.alternatives.evaluation_prompts import role_fitness_prompts, language_level_prompts, language_level_examples, language_level_antiexamples, language_level_rating_examples, language_level_rating_examples_with_reasoning
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
        self.__template = language_level_prompts[prompt_alternative]
        self.__level_description_fname = level_description_fname
        
    def evaluate(self, language, language_level, message, print_prompt=False):
        
        level_description = load_cefr(language_level, self.__level_description_fname)
        
        level_example_string = '\n'.join(language_level_examples[language_level])
        level_antiexample_string = '\n'.join(language_level_antiexamples[language_level])
        #ratings_examples = '\n'.join(language_level_rating_examples[language_level])
        ratings_examples_with_reasoning= '\n'.join(language_level_rating_examples_with_reasoning[language_level]) 
        
        self.__prompt_builder.reset()
        self.__prompt_builder.add_template(self.__template, (language, language_level, level_description, message, level_example_string, level_antiexample_string, ratings_examples_with_reasoning))
        prompt = self.__prompt_builder.build()
        
        if print_prompt:
            print(prompt)
        
        result = self.__thread.send(prompt)
        rating = re.search(r'\d+', result).group()
        
        return int(rating)