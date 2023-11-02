import pandas as pd
import json
import time

from src.bots.refinement_bot import RoleFitnessLanguageLevelBot, RoleFitnessBot, LanguageLevelBot
from src.bot_pipeline import identity_pipeline, make_bot_pipeline
from src.plays import play as bot_play


sampled_settings = pd.read_csv('src/plays/dataset.out', sep=';')
sampled_settings['role_object'] = sampled_settings['role_object'].apply(json.loads)

if 'chat' in sampled_settings:
    sampled_settings['chat'] = sampled_settings['chat'].apply(json.loads)
else:
    sampled_settings['chat'] = [[], ]*18

# TODO define prompt alternatives and pipeline description
prompt_alt_0 = 3
prompt_alt_1 = 2 
pipeline_description = 'RoleFitness('+ str(prompt_alt_0) +')' + 'LanguageLevel(' + str(prompt_alt_1) + ')'


language = 'English'

print(sampled_settings)


try:
    
    chats = sampled_settings['chat']
    
    for idx in range(18):     
        s = sampled_settings.iloc[idx]
        
        if s['chat']:
            continue
        
        ro = s['role_object']    
        
        # TODO define bots and pipeline
        bot_0 = RoleFitnessBot(ro['GPT_role'], ro['user_role'], ro['setting'], prompt_alt_0)
        bot_1 = LanguageLevelBot(s['language_level'], prompt_alt_1)
    
        pipeline = make_bot_pipeline([bot_0.send, bot_1.send, ])
                    
                    
        chat = bot_play.play(ro['setting'], ro['GPT_role'], ro['user_role'], language, s['language_level'], pipeline, 6)      
        
        chats[idx] = chat
        
        print(idx)
        
           
            
    
finally:
    
    sampled_settings['chat'] = chats

    sampled_settings['language'] = [language for i in range(18)]
    sampled_settings['role_object'] = sampled_settings['role_object'].apply(json.dumps)
    sampled_settings['chat'] = sampled_settings['chat'].apply(json.dumps)
    
    sampled_settings['pipeline'] = [pipeline_description for i in range(18)]
     
    fname_out = 'src/plays/dataset.out'
    sampled_settings.to_csv(fname_out, index=False , sep=';')