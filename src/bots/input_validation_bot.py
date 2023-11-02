from bot import Bot
from src.templates.alternatives.user_input_validation import user_input_validation_alternatives

class InputValidationBot(Bot):
    '''Bot performing setting input validation.'''
    
    def __init__(self, alternative=0) -> None:
        super().__init__()
        self.__template = user_input_validation_alternatives[alternative]
        
        
    def send(self, args) :
        '''Sends the formatted input validation prompt to the thread.
        args: tuple - containing the setting description string
        output: boolean - validation result'''
        prompt = self._prompt_builder.add_template(self.__template, args).build()
        self._prompt_builder.reset()
                
        valid = self._thread.send(prompt)
        return valid == '1'