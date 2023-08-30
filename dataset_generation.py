import pandas as pd
import json
import time

from src.bots.refinement_bot import RoleFollowingBot
from src.bot_pipeline import identity_pipeline, make_bot_pipeline
from src.plays import play as bot_play

fname = 'src/plays/roles.out'
settings = pd.read_csv(fname, sep=';')

settings['role_object'] = settings['role_object'].apply(json.loads)

language = 'English'
lang_levels = ['C1', 'C2']


results = pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'])


try:
    for ll in lang_levels:
        sample = settings.sample(n=3)
        
        for s in sample['role_object']:
            
            
            
            # TODO define bots and pipeline
            bot = RoleFollowingBot(s['GPT_role'], s['user_role'], s['setting'])
            pipeline = make_bot_pipeline([bot.send, ])
            #pipeline = identity_pipeline
                        

            # TODO define pipeline description (bot + prompt)

            prompt_alt = 0
            pipeline_description = 'RoleFollowing(' + str(prompt_alt) + ')'

            # TODO adjust prompt to alternative in TEMPLATES !!!
            # TODO make changes in refinement bot
            
                
            chat = bot_play.play(s['setting'], s['GPT_role'], s['user_role'], language, ll, pipeline, 6)
            
            results = pd.concat([ results, pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'], data= [(language, ll, s, pipeline_description, chat ),])])
            
            print('AAAAAAAAAAA')
            time.sleep(10)
    
finally:

    results['role_object'] = results['role_object'].apply(json.dumps)
    results['chat'] = results['chat'].apply(json.dumps)
    
    # TODO update name
    fname_out = 'src/plays/dataset.out'
    results.to_csv(fname_out, index=False , sep=';')