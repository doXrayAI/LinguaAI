import openai
import os
import sys
from keys import OPENAI_API_KEY


sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning")
sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/service")
sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/src") 
sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/src/bots") 
sys.path.append("/home/mihaelabaksic/proj/2023-languagelearning/src/templates") 


openai.api_key = OPENAI_API_KEY
