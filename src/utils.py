import json

def load_template(template_name: str, fname='./src/templates/templates.json'):
    with open(fname) as f:
        data = json.load(f)
        
        if template_name not in data:
            raise ValueError(template_name + " is not a valid template name.")
        
        return data[template_name]
    