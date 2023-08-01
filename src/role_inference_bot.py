from prompt_builder import PromptBuilder
from single_run_thread import SingleRunThread
from utils import load_template
import json



class RoleInferenceBot:

    def __init__(self) -> None:
        self.__prompt_builder = PromptBuilder()
        self.__thread = SingleRunThread()
        self.__template = dict()
        self.__template['description'] = load_template('role_inference_description')
        self.__template['examples'] = load_template('role_inference_examples')
        self.__template['query'] = load_template('role_inference_query')
        
        self.__prompt_builder.add_template(self.__template['description']['template'], ())
        self.__prompt_builder.add_template(self.__template['examples']['template'], ())
        self.__prompt_builder.add_template(self.__template['examples']['choices'][1], ())
        self.__prompt_builder.add_template(self.__template['examples']['choices'][3], ())
        self.__prompt_builder.add_template(self.__template['examples']['choices'][4], ())
        
        
        
    def infere(self, description: str) -> dict():

        self.__prompt_builder.add_template(self.__template['query']['template'], (description, ))
        
        prompt = self.__prompt_builder.build()
        self.__prompt_builder.pop()
        
        result = self.__thread.send(prompt).replace('\n', '') 
        
        # convert result to dict
        try:
            roles = json.loads('{' + result + '}')
            
            if 'setting' not in roles:
                roles['setting'] = description
            
            return roles
        
        except json.decoder.JSONDecodeError:
            print(result)
            return None
