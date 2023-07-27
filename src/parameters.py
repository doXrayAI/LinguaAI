from collections import namedtuple


GPTParameters = namedtuple('GPTParameters'
                 , [ 'model', 'temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty', 'stop']
                 , defaults=('gpt-3.5-turbo', 0.7, 800, 0.95, 0, 0, None)
                 )



default_chat_completion_parameters = GPTParameters()
default_completion_parameters = GPTParameters('text-davinci-003', 0.2, 800, 0.95, 0, 0, None)

default_system_prompt = "You are an AI assistant that helps people find information."