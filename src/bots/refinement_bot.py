from bot import Bot
from utils import load_template, load_cefr
from src.templates.alternatives.role_fitness_bot import role_fitness_refinement_alternatives
from src.templates.alternatives.role_fitness_language_level_bot import role_fitness_language_level_refinement_alternatives
from src.templates.alternatives.language_level_bot import language_level_refinement_alternatives, language_level_examples

class LanguageLevelBot(Bot):
    '''Refining the input to match given language level'''
    
    def __init__(self, language_level, language, alternative):
        super().__init__()
        self.__template = dict()

        self.__template = language_level_refinement_alternatives[alternative]
        language_level_description = load_cefr(language_level)
        
        # The examples functionality is currently only supported for English
        examples = ''
        if language == 'English':
            examples += ' Examples of {0} language level sentences in {1}: '.format(language_level, language)
            examples += '\n'.join(language_level_examples[language_level])
        
        self._prompt_builder.add_template(self.__template, (language_level, language_level_description, examples, language))
        
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement'''
        self._prompt_builder.add_template(args)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
                
        refinement = self._thread.send(prompt)
        history.append(refinement)
        return refinement, history
    
    
class LanguageLevelSimplificationBot(LanguageLevelBot):
    
    def __init__(self, language_level, language):
        super().__init__(language_level, language, alternative=4) # alternative 4 is for language simplification
        self.__language_level = language_level
        
    def send(self, args, history):
        if self.__language_level in ['A1', 'A2']: # only simplify A1 and A2 language levels
            return super().send(args, history)
        
        history.append(args)
        return args, history
    
class RoleFitnessBot(Bot):
    '''Refining the input to match the GPT and user role'''
    
    def __init__(self, GPT_role, user_role, setting, alternative=0):
        super().__init__()
        self.__template = dict()
        
        self.__template = role_fitness_refinement_alternatives[alternative]
                
        self._prompt_builder.add_template(self.__template, (GPT_role, user_role, setting))
        
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement.'''
        
        self._prompt_builder.add_template(args)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        history.append(refinement)
        return refinement, history
    
    
    
    
class UserEngagementBot(Bot):
    '''Refining the input to incite further user engagement.'''
    
    def __init__(self, GPT_role, user_role, setting):
        super().__init__()
        self.__template = dict()
        self.__template = load_template('user_engagement_refinement')
        self._prompt_builder.add_template(self.__template['template'], (GPT_role, user_role, setting))
        
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement.'''

        self._prompt_builder.add_template(args)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        history.append(refinement)
        return refinement, history
    
    
    
class RoleFitnessLanguageLevelBot(Bot):
    
    def __init__(self, GPT_role, user_role, language_level, alternative=0):
        
        super().__init__()
        self.__template = dict()
        self.__template = role_fitness_language_level_refinement_alternatives[alternative]
        
        cefr_description = load_cefr(language_level)
        self._prompt_builder.add_template(self.__template, ( GPT_role, user_role, language_level, cefr_description))
                
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement.'''

        self._prompt_builder.add_template(args)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
                
        refinement = self._thread.send(prompt)
        history.append(refinement)
        return refinement, history
    