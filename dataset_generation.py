import pandas as pd
import json

from src.bots.refinement_bot import LanguageLevelRefinementBot
from src.bot_pipeline import identity_pipeline, make_bot_pipeline
from src.plays import play as bot_play

fname = 'src/plays/roles.out'
settings = pd.read_csv(fname, sep=';')

settings['role_object'] = settings['role_object'].apply(json.loads)

language = 'English'
lang_levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']



results = pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'])


try:
    for ll in lang_levels:
        sample = settings.sample(n=3)
        
        for s in sample['role_object']:
            
            # TODO define bots and pipeline
            bot = LanguageLevelRefinementBot(ll)
            pipeline = make_bot_pipeline([bot.send, ])
            

            # TODO define pipeline description (bot + prompt)
            prompt = "Rephrase the text to be on {0} level of CEFR language proficiency. The {0} level is defined as: {1}.\n\nExamples of reasoning:\n\nSentence-> Lab supervisor: There is no way this can be achieved in just under 20 minutes, they must have gone mad.\nLevel-> A1\nThought-> Is there too complex vocabulary? Can the grammar be simplified? Can the most basic user understand this?\nRephrasing-> Lab supervisor: They could not do this in 20 minutes. They are crazy.\n\nSentence-> Comentator: Football matches can create great atmosphere in stadiums because football is competitive.\nLevel->  C1\nThought-> Can the grammar and vocabulary be improved? Does it fit C1 knowledge?\nRephrasing-> Comentator: The intensity and competitiveness of football matches can create an electrifying atmosphere in stadiums.\n\nRephrase the text to be on a {0} level. Only output the rephrasing."
    
            pipeline_description = 'LanguageLevelBot(' + prompt + ')'

            # TODO adjust prompt to alternative in TEMPLATES !!!
            # TODO make changes in refinement bot
            
                
            chat = bot_play.play(s['setting'], s['GPT_role'], s['user_role'], language, ll, pipeline, 6)
            
            results = pd.concat([ results, pd.DataFrame(columns=['language', 'language_level', 'role_object', 'pipeline', 'chat'], data= [(language, ll, s, pipeline_description, chat ),])])
            

    
finally:

    results['role_object'] = results['role_object'].apply(json.dumps)
    results['chat'] = results['chat'].apply(json.dumps)
    
    # TODO update name
    fname_out = 'src/plays/language_level.out'
    results.to_csv(fname_out, index=False , sep=';')