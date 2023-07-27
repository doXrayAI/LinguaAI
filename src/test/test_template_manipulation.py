import unittest
from src.utils import load_template

class TestTemplateManipulation(unittest.TestCase):
    
    
    def test_template_loading(self):
        t = load_template('setting_user_input_validation')
        
        self.assertEqual(t['template'],"Does the following describe a situation, place or activity? Respond only with 1 or 0.  {}",
)
        self.assertEqual(t['n_args'], 1)
        
        
    def test_missing_template_loading(self):
        
        self.assertRaises(ValueError, lambda: load_template('inexistent_template'))