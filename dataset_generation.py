import pandas as pd
import json
import time

from src.bots.refinement_bot import RoleFitnessLanguageLevelBot
from src.bot_pipeline import identity_pipeline, make_bot_pipeline
from src.plays import play as bot_play

fname = 'src/plays/roles.out'
settings = pd.read_csv(fname, sep=';')

settings['role_object'] = settings['role_object'].apply(json.loads)

language = 'English'
lang_levels = ['A1', 'A2', 'B1']


results = pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'])


try:
    for ll in lang_levels:
        sample = settings.sample(n=3)
        
        for s in sample['role_object']:
            
            
            # TODO define bots and pipeline
            prompt_alt = 2 
            bot = RoleFitnessLanguageLevelBot(s['GPT_role'], s['user_role'], ll, prompt_alt)
            pipeline = make_bot_pipeline([bot.send, ])
            #pipeline = identity_pipeline
                        
            
            pipeline_description = 'RoleFitnessLangugeLevel(' + str(prompt_alt) + ')'

            # TODO make changes in refinement bot
                            
            chat = bot_play.play(s['setting'], s['GPT_role'], s['user_role'], language, ll, pipeline, 6)
            
            results = pd.concat([ results, pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'], data= [(language, ll, s, pipeline_description, chat ),])])
            
            print('AAAAAAAAAAA')
            time.sleep(60)
            
    
finally:

    results['role_object'] = results['role_object'].apply(json.dumps)
    results['chat'] = results['chat'].apply(json.dumps)
    
    # TODO update name
    fname_out = 'src/plays/dataset.out'
    results.to_csv(fname_out, index=False , sep=';')