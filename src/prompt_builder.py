from collections import namedtuple


UnformattedString = namedtuple('UnformattedString', ['string', 'arguments'])


class PromptBuilder:
    
    def __init__(self):
        self.__templates = []
    
    def add_template(self, input: str, args: tuple):
        self.__templates.append( UnformattedString(input, args))
        return self
        
    def build(self) -> str:
        return '\n'.join([ template.string.format(*template.arguments) for template in self.__templates])
    
    
    def reset(self):
        self.__templates = [] 
        
        