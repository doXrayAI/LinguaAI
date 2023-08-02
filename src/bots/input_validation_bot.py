from utils import load_template
from bot import Bot


class InputValidationBot(Bot):
    
    def __init__(self) -> None:
        super().__init__()
        self.__template = load_template('setting_user_input_validation')
        
        
    def send(self, args) :
        prompt = self._prompt_builder.add_template(self.__template['template'], args).build()
        self._prompt_builder.reset()
        
        valid = self._thread.send(prompt)
        return valid == '1'