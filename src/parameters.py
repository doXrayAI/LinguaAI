from collections import namedtuple


GPTParameters = namedtuple('GPTParameters'
                 , [ 'model', 'temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty', 'stop']
                 , defaults=('gpt-3.5-turbo', 0.7, 800, 0.95, 0, 0, None)
                 )



default_parameters = GPTParameters()
creative_parameters = GPTParameters(temperature=0.7, top_p=0.8)

default_system_prompt = "You are an AI assistant that helps people find information."