import pandas as pd
import json

from src.bots.evaluation_bot import LanguageLevelEvaluationBot


fname = 'src/plays/language_level/language_level_0.out'

fname_out = 'src/plays/evaluation/language_level_0.out'

df = pd.read_csv(fname, sep=';')
df['role_object'] = df['role_object'].apply(json.loads)
df['chat'] = df['chat'].apply(json.loads)


evaluator = LanguageLevelEvaluationBot(6, 'src/templates/language_levels_cefr.json')

ratings_all = []


for idx, dialogue in df.iterrows():
    context = dialogue['role_object']
    
    messages_for_evaluation = dialogue['chat'][2::2]
    
    ratings = []

    for m in messages_for_evaluation:
        ratings.append(evaluator.evaluate( dialogue['language'], dialogue['language_level'], m))
        
    ratings_all.append(ratings)
    print(ratings)
    
    
df = pd.DataFrame(data=ratings_all, columns=['language_level'])
df.to_csv(fname=fname_out)