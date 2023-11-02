from src.bots.chatbot import ChatBot

class ChatBotOperator:
    '''Operates and synchronises a stateful chatbot and auxiliary bots in a pipeline'''
    
    def __init__(self, chatbot, pipeline) -> None:
        self.__chatbot = chatbot
        self.__refinement_pipeline = pipeline
        
        
    def chatbot_setup(self, initial_user_message = None) -> str:
        '''Adds initial chatbot message'''
        response = self.__chatbot.send()
        
        # If initial user message is given, add it to the message list and require new response
        if initial_user_message:
            self.__chatbot.add_message(initial_user_message, 'user')
            response = self.__chatbot.send()
        
        # Add the refined GPT response to the list
        refined_response, history = self.__refinement_pipeline(response['content'], [response['content'],])
        
        self.__chatbot.add_message(refined_response, role='assistant')
                
        return refined_response
    
    
    def send_message(self, message) -> str:
        '''Sends user message to chatbot, performs pipeline operations on the response, 
        stores the refined refined response and returns it'''
        self.__chatbot.add_message(message, 'user')
        
        response = self.__chatbot.send()
        
        refined_response, history = self.__refinement_pipeline(response['content'], [response['content'],])
                
        self.__chatbot.add_message(refined_response, role='assistant')
                
        return refined_response
    
    
    def get_chat(self):
        return self.__chatbot.get_chat()
    
    def get_dialogue_length(self):
        return self.__chatbot.get_dialogue_length()
    
    def get_dialogue_string(self, window):
        return self.__chatbot.get_dialogue_string(window)
        