import json

"""Utility module"""

prompt_templates = dict()
cefr_descriptions = dict()

def load_template(template_name: str, fname='./src/templates/templates.json'):
    '''Loads template with template_name from the templates.json file.
        The fname argument defines the templates loction.
        If template with template_name does not exist, rairses ValueError'''
    global prompt_templates
    
    if not prompt_templates:
        with open(fname) as f:
            prompt_templates = json.load(f)
        
    if template_name not in prompt_templates:
        raise ValueError(template_name + " is not a valid template name.")

    return prompt_templates[template_name]
    
    
    
def load_cefr(level: str, fname='./src/templates/language_levels_cefr.json'):
    ''' Loads CEFR language level description from the language_levels_cefr.json file.
        The fname argument defines the language description loction.
        If CEFR level named level does not exist, raises ValueError'''
    global cefr_descriptions
    
    if not cefr_descriptions:
        with open(fname) as f:
            cefr_descriptions = json.load(f)
        
    if level not in cefr_descriptions:
        raise ValueError(level + " is not a valid CEFR level")

    return cefr_descriptions[level]