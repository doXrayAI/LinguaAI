import unittest
from src.thread import Thread
from src.parameters import default_system_prompt

class TestThread(unittest.TestCase):
    
    def test_default_system_prompt(self):
        t = Thread()
        
        self.assertEqual(t.get_messages()[0].role, 'system')
        self.assertEqual(t.get_messages()[0].content, default_system_prompt)
        
        
    def test_custom_system_prompt(self):
        custom_system_prompt = 'You are GPT model. Assist users with questions'
        t = Thread(custom_system_prompt)
        
        self.assertEqual(t.get_messages()[0].role, 'system')
        self.assertEqual(t.get_messages()[0].content, custom_system_prompt)
        
        
    def test_adding_user_prompt(self):
        t = Thread()
        user_prompt = 'Write 2 sentences about Robert Oppenheimer.'
        t.add_user_prompt(user_prompt)
        
        self.assertEqual(t.get_messages()[1].role, 'user')
        self.assertEqual(t.get_messages()[1].content, user_prompt)
        
        
    def test_sending(self):
        t = Thread()
        user_prompt = 'Write 2 sentences about Robert Oppenheimer.'
        t.add_user_prompt(user_prompt)
        
        response = t.send()
        self.assertEqual(response.role, 'assistant')
        t.add_assistant_prompt(response.content)
        
        messages = t.get_messages()
        self.assertEqual(messages[2].role, 'assistant')
        
        