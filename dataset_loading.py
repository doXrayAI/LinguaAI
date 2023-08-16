import pandas as pd
import json


fname = 'src/plays/role_fitness/role_fitness_1.out'

df = pd.read_csv(fname, sep=';')

df['role_object'] = df['role_object'].apply(json.loads)
df['chat'] = df['chat'].apply(json.loads)

print(df['language_level'])

for chat in df['chat'] :
    for m_idx in range(2, len(chat)):
        print(chat[m_idx]['content'])
        print('...')
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    
    
