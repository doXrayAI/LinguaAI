from collections import namedtuple


UnformattedString = namedtuple('UnformattedString', ['string', 'arguments'])


class PromptBuilder:
    '''Building prompts from templates'''
    
    def __init__(self):
        self.__templates = []
        
    
    def add_template(self, input: str, args: tuple=()):
        '''Adding a template and its arguments to template list'''
        self.__templates.append( UnformattedString(input, args))
        return self
        
        
    def build(self) -> str:
        '''Building a single prompt string from added templates and arguments'''
        return '\n'.join([ template.string.format(*template.arguments) for template in self.__templates])
    
    
    def reset(self):
        '''Clears template list'''
        self.__templates = [] 
        
        
    def pop(self):
        '''Removes and returns last template from the list'''
        if len(self.__templates) > 0:
            return self.__templates.pop()
        
        return None
        