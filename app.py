from flask import Flask, render_template, request, jsonify
from src.bots.input_validation_bot import InputValidationBot
from src.bots.role_inference_bot import RoleInferenceBot
import service.services as services

app = Flask(__name__)

role_inference_bot = RoleInferenceBot()
input_validation_bot = InputValidationBot()

@app.route('/')
def index():
    return render_template('index.html')
    
    

@app.route('/context/<language>/<language_level>/<setting_description>')
def assert_context(language, language_level, setting_description):
    
    valid_input = input_validation_bot.send((setting_description,))
        
    res = {'content': valid_input}
    return jsonify(res)


@app.route('/roles/<setting_description>')
def get(setting_description):
    
    roles = role_inference_bot.send((setting_description,))
    return jsonify(roles)
    
    
    
@app.route('/new_chat/<setting>/<GPT_role>/<user_role>/<language>/<language_level>')
def new_chat(setting, GPT_role, user_role, language, language_level):
    res = services.add_new_chat(setting, GPT_role, user_role, language, language_level)
    return jsonify(res)
    
    
@app.route('/chats')
def get_chats():
    return jsonify(services.get_chats())
    
    
@app.route('/chat_messages/<chat_id>')
def get_chat_messages(chat_id = '0'):
    return jsonify(services.get_chat_messages(chat_id))
    
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3002, debug=True)



