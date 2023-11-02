import unittest
from src.single_run_thread import SingleRunThread

class TestSingleRunThread(unittest.TestCase):
    
    def test_send(self):
        t = SingleRunThread()
        
        res = t.send("2+3=")
        self.assertEqual(res, '5')
        
        
    