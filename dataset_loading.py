import pandas as pd
import json


fname = 'src/plays/language_level_role_fitness.out'

df = pd.read_csv(fname, sep=';')

df['role_object'] = df['role_object'].apply(json.loads)
df['chat'] = df['chat'].apply(json.loads)


print(len(df['chat']))
print(df['language_level'])

for c in df.iloc[-1]['chat'] :
    print(c['content'])
    print('-------------------------------------------------------------')
    
