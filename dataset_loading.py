import pandas as pd
import json


fname = 'src/plays/gpt-4/language_level_role_fitness/ll_rf_aaaaa.out'

df = pd.read_csv(fname, sep=';')

df['role_object'] = df['role_object'].apply(json.loads)
df['chat'] = df['chat'].apply(json.loads)

print(df['language_level'])
print(len(df))

for chat in df['chat'] :
    for m_idx in range(2, len(chat)):
        print(chat[m_idx]['content'])
        print('...')
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')
