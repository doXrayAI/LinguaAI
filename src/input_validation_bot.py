from prompt_builder import PromptBuilder
from single_run_thread import SingleRunThread
from utils import load_template


class InputValidationBot:
    
    def __init__(self) -> None:
        self.__prompt_builder = PromptBuilder()
        self.__thread = SingleRunThread()
        self.__template = load_template('setting_user_input_validation')
        
        
    def validate(self, description: str) -> bool:
        prompt = self.__prompt_builder.add_template(self.__template['template'], (description,)).build()
        self.__prompt_builder.reset()
        
        valid = self.__thread.send(prompt)
        return valid == '1'