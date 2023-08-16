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
lang_levels = [ 'C1', 'C2']


results = pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'])


try:
    for ll in lang_levels:
        sample = settings.sample(n=2)
        
        for s in sample['role_object']:
            
            # TODO define bots and pipeline
            bot = RoleFollowingBot(s['GPT_role'], s['user_role'], s['setting'])
            pipeline = make_bot_pipeline([bot.send, ])
                        

            # TODO define pipeline description (bot + prompt)
            prompt = "Act as a {0}. You are speaking to {1}. Make minimal changes to the tone and voice of the provided sentence to sound more like {0}\n Examples:\nWaiter: Hi, what do you want?-> Waiter: Hi, what can I offer you today?\nPoliceman: Lady, what happened here? -> Policeman: Ma'am, could you rpovide more information about the situation?"

            pipeline_description = 'RoleFollowingBot(' + prompt + ')'
            #pipeline_description = 'Identity'

            # TODO adjust prompt to alternative in TEMPLATES !!!
            # TODO make changes in refinement bot
            
                
            chat = bot_play.play(s['setting'], s['GPT_role'], s['user_role'], language, ll, pipeline, 6)
            
            results = pd.concat([ results, pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'], data= [(language, ll, s, pipeline_description, chat ),])])
            

    
finally:

    results['role_object'] = results['role_object'].apply(json.dumps)
    results['chat'] = results['chat'].apply(json.dumps)
    
    # TODO update name
    fname_out = 'src/plays/dataset.out'
    results.to_csv(fname_out, index=False , sep=';')