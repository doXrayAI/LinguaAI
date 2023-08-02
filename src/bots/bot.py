from abc import ABC, abstractmethod

from prompt_builder import PromptBuilder
from single_run_thread import SingleRunThread

class Bot(ABC):
    '''Generic abstract bot, holds a PromptBuilder and a Thread or SingleRunThread'''
    
    def __init__(self, thread = SingleRunThread()) -> None:
        self._prompt_builder = PromptBuilder()
        self._thread = thread
        
    
    @abstractmethod
    def send(self, args, history):
        pass