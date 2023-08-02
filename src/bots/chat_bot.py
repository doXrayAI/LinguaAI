from bot import Bot
from thread import Thread

class ChatBot(Bot):
    
    def __init__(self, setting_description, language='english', language_level='A1') -> None:
        super().__init__(thread=Thread())
        
        
    def send(self, args):
        ...
        
        
    def add_response(self, message, role= 'user' | 'assistant'):
        ...