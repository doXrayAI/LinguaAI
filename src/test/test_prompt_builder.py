import unittest

from src.prompt_builder import PromptBuilder


class PromptBuilderTest(unittest.TestCase):
    
    def test_single_argument(self):
        b = PromptBuilder()
        b = b.add_template('Hello GPT, my name is {}', (11,) )
        built_prompt = b.build()
        
        self.assertEqual(built_prompt, "Hello GPT, my name is 11")
    
    def test_no_prompts(self):
        b = PromptBuilder()
        built_prompt = b.build()
        self.assertEqual(built_prompt, '')
        
        
    def test_multiple_templates(self):
        b = PromptBuilder()
        b.add_template('Template {}', (1,)).add_template('Template {}', (2,))
        prompt = b.build()
        self.assertEqual(prompt, 'Template 1\nTemplate 2')
        
        
    def test_n_args_0(self):
        b = PromptBuilder()
        b.add_template("Template with no args", ())
        
    def test_noniterable_argument(self):
        b = PromptBuilder()
        b.add_template('This isn\'t iterable {}', 11)
        self.assertRaises(TypeError, b.build)
        
    def test_reset(self):
        b = PromptBuilder()
        b = b.add_template('Basic template {} {}', (10, 11))
        built_prompt = b.build()
        self.assertEqual(built_prompt, 'Basic template 10 11')
        
        b.reset()
        built_prompt = b.build()
        self.assertEqual(built_prompt, '')
        