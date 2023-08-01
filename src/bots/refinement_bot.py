from bot import Bot
from utils import load_template, load_cefr


class LanguageLevelRefinementBot(Bot):
    
    def __init__(self, language_level):
        super().__init__()
        self.__template = dict()
        self.__template = load_template('language_level_refinement')
        language_level_description = load_cefr(language_level)
        self._prompt_builder.add_template(self.__template['template'], (language_level, language_level_description))
        
        
    def send(self, input) :
        
        self._prompt_builder.add_template(input)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        return refinement
    
    
    
class RoleFollowingBot(Bot):
    
    def __init__(self, GPT_role, user_role):
        super().__init__()
        self.__template = dict()
        self.__template = load_template('role_following_refinement')
        self._prompt_builder.add_template(self.__template['template'], (GPT_role, user_role))
        
        
    def send(self, input) :
        
        self._prompt_builder.add_template(input)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        return refinement
    
    
    
    
class UserEngagementBot(Bot):
    
    def __init__(self, GPT_role, user_role, setting):
        super().__init__()
        self.__template = dict()
        self.__template = load_template('user_engagement_refinement')
        self._prompt_builder.add_template(self.__template['template'], (GPT_role, user_role, setting))
        
        
    def send(self, input) :
        
        self._prompt_builder.add_template(input)
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        refinement = self._thread.send(prompt)
        return refinement