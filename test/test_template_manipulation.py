import unittest
from src.utils import load_template

class TestTemplateManipulation(unittest.TestCase):
    
    
    def test_template_loading(self):
        t = load_template('setting_user_input_validation')
        
        self.assertEqual(t['template'],"Is the following a description of a place, situation or activity involving people? \"{}\"  Respond only with 1 if it clearly does, otherwise 0.",
)
        self.assertEqual(t['n_args'], 1)
        
        
    def test_missing_template_loading(self):
        
        self.assertRaises(ValueError, lambda: load_template('inexistent_template'))