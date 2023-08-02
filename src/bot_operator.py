from src.bots.chatbot import ChatBot

class ChatBotOperator:
    '''Operates and synchronises a chatbot and auxiliary bots in a pipeline'''
    
    def __init__(self, chatbot, pipeline) -> None:
        self.__chatbot = chatbot
        self.__refinement_pipeline = pipeline
        
        
    def chatbot_setup(self) -> str:
        '''Adds initial chatbot message'''
        response = self.__chatbot.send()
        
        refined_response, history = self.__refinement_pipeline(response.content, [])
        
        self.__chatbot.add_message(refined_response, role='assistant')
        
        return refined_response
    
    
    def send_message(self, message) -> str:
        '''Sends user message to chatbot, performs pipeline operations on the response, 
        stores the refined refined response and returns it'''
        self.__chatbot.add_message(message, 'user')
        
        response = self.__chatbot.send()
        
        refined_response, history = self.__refinement_pipeline(response.content, [response.content,])
                
        self.__chatbot.add_message(refined_response, role='assistant')
        
        return refined_response