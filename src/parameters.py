from collections import namedtuple


GPTParameters = namedtuple('GPTParameters'
                 , ['engine', 'model', 'temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty', 'stop']
                 , defaults=('paper2podcast_dev','gpt-3.5-turbo', 0.7, 800, 0.95, 0, 0, None)
                 )

default_gpt_parameters = GPTParameters()

default_system_prompt = "You are an AI assistant that helps people find information."