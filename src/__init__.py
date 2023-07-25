import openai
import os


openai.api_type = 'azure'
openai.api_base = "https://doxray-openai-west-europe.openai.azure.com/"
openai.api_version = "2023-03-15-preview"

openai.api_key = os.getenv("OPENAI_API_KEY")