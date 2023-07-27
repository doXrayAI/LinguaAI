import unittest
from src.completion_thread import CompletionThread

class TestCompletionThread(unittest.TestCase):
    
    def test_send(self):
        t = CompletionThread()
        
        res = t.send("2+3=")
        self.assertEqual(res, '5')
        
        
    