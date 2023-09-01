import pandas as pd
import json

from src.bots.evaluation_bot import LanguageLevelEvaluationBot, RoleFitnessEvaluationBot


fname = 'src/plays/gpt-4/language_level_role_fitness/language_level_role_fitness_2.out'

fname_out = 'src/plays/gpt-4/evaluation/ev.out'

df = pd.read_csv(fname, sep=';')
df['role_object'] = df['role_object'].apply(json.loads)
df['chat'] = df['chat'].apply(json.loads)


evaluator = LanguageLevelEvaluationBot(6, 'src/templates/language_levels_cefr.json')
#evaluator = RoleFitnessEvaluationBot(2)

ratings_all = []

try:
    for idx, dialogue in df.iterrows():
        context = dialogue['role_object']
        
        ratings = []
        
        for i in range(2, len(dialogue['chat']), 2):
            prev_messages = '\n'.join(a['content'] for a in dialogue['chat'][2:i])
            message = dialogue['chat'][i]['content']
            
            ratings.append(evaluator.evaluate(dialogue['language'], dialogue['language_level'], message))
            
        ratings_all.append(ratings)
        print(ratings)

finally:
    
    df = pd.DataFrame(data=ratings_all, columns=['language_level'])
    df.to_csv(fname=fname_out)