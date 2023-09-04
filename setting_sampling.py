import pandas as pd
import json
import time

from src.bots.refinement_bot import RoleFitnessLanguageLevelBot
from src.bot_pipeline import identity_pipeline, make_bot_pipeline
from src.plays import play as bot_play

fname = 'src/plays/roles.out'
settings = pd.read_csv(fname, sep=';')
settings['role_object'] = settings['role_object'].apply(json.loads)


results = pd.DataFrame(columns=['language', 'language_level', 'role_object', 'chat'])


language = 'English'
lang_levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

try:
    
    for ll in lang_levels:
        sample = settings.sample(n=3)
        
        results = pd.concat([results, pd.DataFrame(columns=['role_object'], data=sample['role_object'])])
            
    
finally:
    
        results['role_object'] = results['role_object'].apply(json.dumps)
        
        results['language'] = [language for i in range(18)]
        results['language_level'] = [lang_levels[i//3] for i in range(18) ]
        results['chat'] = [[], ]*18       
        
        fname_out = 'src/plays/sampled_settings.out'
        results.to_csv(fname_out, index=False , sep=';')