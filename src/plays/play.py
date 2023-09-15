from single_run_thread import SingleRunThread
from prompt_builder import PromptBuilder
from utils import load_template, load_cefr
from parameters import GPTParameters
from src.bot_pipeline import make_bot_pipeline, identity_pipeline
import keys
from src.bot_operator import ChatBotOperator, ChatBot
import openai

openai.api_key = keys.OPENAI_API_KEY


def play(setting, GPT_role, user_role, language, language_level, pipeline, n_turns=10):
    '''Conducts a dialogue between two chatbots
    The argument pipeline is applied to the first chatbot. An identity pipeline is applied to the second bot.
    The argument n_turns defines the number of turns bots take.'''

    chatbot_1 = ChatBot(setting, GPT_role, user_role, language, language_level)
        
    # Reversed roles
    chatbot_2 = ChatBot(setting, user_role, GPT_role, language, language_level)
    
    chatbot_operator_1 = ChatBotOperator(chatbot_1, pipeline)
    chatbot_operator_2 = ChatBotOperator(chatbot_2, identity_pipeline)
    
    message = chatbot_operator_1.chatbot_setup()
    message = chatbot_operator_2.chatbot_setup(initial_user_message=message)
    
    for i in range(n_turns - 1):
        message = chatbot_operator_1.send_message(message)
        message = chatbot_operator_2.send_message(message)
        
    return chatbot_operator_2.get_chat()

