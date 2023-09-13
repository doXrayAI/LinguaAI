from flask import Flask, render_template, request, jsonify
from src.bots.input_validation_bot import InputValidationBot
from src.bots.role_inference_bot import RoleInferenceBot
import app.services as services

app = Flask(__name__)

role_inference_bot = RoleInferenceBot()
input_validation_bot = InputValidationBot()


@app.route('/')
def index():
    return render_template('index.html')
    
# Route asserting the new chat context    
@app.route('/context/<language>/<language_level>/<setting_description>')
def assert_context(language, language_level, setting_description):
    
    valid_input = input_validation_bot.send((setting_description,))
        
    res = {'content': valid_input}
    return jsonify(res)

# Route infering roles based ona a setting description
@app.route('/roles/<setting_description>')
def get(setting_description):
    roles = role_inference_bot.send((setting_description,))
    return jsonify(roles)
    
    
# Route initializing and returning a new chat    
@app.route('/new_chat/<setting>/<GPT_role>/<user_role>/<language>/<language_level>')
def new_chat(setting, GPT_role, user_role, language, language_level):
    res = services.add_new_chat(setting, GPT_role, user_role, language, language_level)
    return jsonify(res)
    
# Route fetching chat contexts
@app.route('/chats')
def get_chats():
    return jsonify(services.get_chats())
    
# Route fetching chat contexts and messages    
@app.route('/chat_messages/<chat_id>')
def get_chat_messages(chat_id = '0'):
    return jsonify(services.get_chat_messages(chat_id))


# Route sending a new user message for an existing chat
@app.route('/new_message/<message>/<chat_id>')
def new_message(message, chat_id=0):
    return jsonify(services.new_message(message, chat_id))
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001, debug=True)



