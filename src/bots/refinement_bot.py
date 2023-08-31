from bot import Bot
from utils import load_template, load_cefr
from time import sleep
from src.templates.alternatives.role_fitness_bot import role_fitness_refinement_alternatives
from src.templates.alternatives.role_fitness_language_level_bot import role_fitness_language_level_refinement_alternatives
from src.templates.alternatives.language_level_bot import language_level_refinement_alternatives

class LanguageLevelRefinementBot(Bot):
    '''Refining the input to match given language level'''
    
    def __init__(self, language_level, alternative):
        super().__init__()
        self.__template = dict()
        #self.__template = load_template('language_level_refinement')
        self.__template = language_level_refinement_alternatives[alternative]
        language_level_description = load_cefr(language_level)
        
        self._prompt_builder.add_template(self.__template, (language_level, language_level_description))
        
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement'''
        self._prompt_builder.add_template(args)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        history.append(refinement)
        return refinement, history
    
    
    
class RoleFollowingBot(Bot):
    '''Refining the input to match the GPT and user role'''
    
    def __init__(self, GPT_role, user_role, setting, alternative=0):
        super().__init__()
        self.__template = dict()
        
        #self.__template = load_template('role_following_refinement')
        self.__template = role_fitness_refinement_alternatives[alternative]
        
        print(self.__template)
        
        self._prompt_builder.add_template(self.__template, (GPT_role, user_role, setting))
        
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement.'''
        
        sleep(20)

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
        #self.__template = load_template('role_fitness_language_level_refinement')
        self.__template = role_fitness_language_level_refinement_alternatives[alternative]
        
        cefr_description = load_cefr(language_level)
        self._prompt_builder.add_template(self.__template, ( language_level, cefr_description, GPT_role, user_role))
        
        
    def send(self, args, history) :
        '''Accepts the input string as args, stores refinement to history and returns the refinement.'''

        self._prompt_builder.add_template(args)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        history.append(refinement)
        return refinement, history
    