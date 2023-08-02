from bots.chat_bot import ChatBot

class ChatBotOperator:
    
    def __init__(self, chatbot, pipeline) -> None:
        self.__chatbot = chatbot
        self.__refinement_pipeline = pipeline
        
    def chatbot_setup(self) -> str:
        gpt_response = self.__chatbot.send()
        
        refined_response, history = self.__refinement_pipeline(gpt_response.content, [])
        print(history)
        
        self.__chatbot.add_message(refined_response, role='assistant')
        
        return refined_response
    
    
    
    def send_message(self, message) -> str:
        self.__chatbot.add_message(message, 'user')
        
        gpt_response = self.__chatbot.send()
        
        refined_response, history = self.__refinement_pipeline(gpt_response.content, [gpt_response.content,])
                
        self.__chatbot.add_message(refined_response, role='assistant')
        
        return refined_response