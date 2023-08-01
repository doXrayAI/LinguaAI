from prompt_builder import PromptBuilder
from single_run_thread import SingleRunThread
from utils import load_template
from bot import Bot
import json



class RoleInferenceBot(Bot):

    def __init__(self) -> None:
        super().__init__()
        self.__template = dict()
        self.__template['description'] = load_template('role_inference_description')
        self.__template['examples'] = load_template('role_inference_examples')
        self.__template['query'] = load_template('role_inference_query')
        
        self._prompt_builder.add_template(self.__template['description']['template'])
        self._prompt_builder.add_template(self.__template['examples']['template'])
        self._prompt_builder.add_template(self.__template['examples']['choices'][1])
        self._prompt_builder.add_template(self.__template['examples']['choices'][3])
        self._prompt_builder.add_template(self.__template['examples']['choices'][4])
        
        
        
    def send(self, args):

        self._prompt_builder.add_template(self.__template['query']['template'], args)
        
        prompt = self._prompt_builder.build()
        self._prompt_builder.pop()
        
        result = self._thread.send(prompt).replace('\n', '') 
        
        # convert result to dict
        try:
            roles = json.loads('{' + result + '}')
            
            if 'setting' not in roles:
                roles['setting'] = args[0]
            
            return roles
        
        except json.decoder.JSONDecodeError:
            print('Cannot decode roles: ' + result)
            return None
