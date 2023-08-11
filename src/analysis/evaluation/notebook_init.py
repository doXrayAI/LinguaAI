

def notebook_init():
    import sys
    sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning")
    sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/src") 
    sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/src/templates") 
    sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/src/templates/alternatives") 



    
    
    
def notebook_imports():
    from single_run_thread import SingleRunThread
    from prompt_builder import PromptBuilder
    from utils import load_template, load_cefr
    from parameters import GPTParameters
    import keys

    import openai

    openai.api_key = keys.OPENAI_API_KEY