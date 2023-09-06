from flask import Flask, render_template, request, jsonify
from src.bots.input_validation_bot import InputValidationBot
from src.bots.role_inference_bot import RoleInferenceBot

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template('index.html')
    
    

@app.route('/context/<language>/<language_level>/<setting_description>')
def assert_context(language, language_level, setting_description):
    
    bot = InputValidationBot()
    valid_input = bot.send((setting_description,))
    
    print(setting_description + '; valid: ' + str(valid_input))
    
    res = {'content': valid_input}
    return jsonify(res)


@app.route('/roles/<setting_description>')
def get(setting_description):
    
    bot = RoleInferenceBot()
    
    roles = bot.send((setting_description,))
    print(roles)
    
    res = {'content': roles}
    return jsonify(res)
    
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)



