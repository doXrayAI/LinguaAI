import pandas as pd
import json


fname = 'src/plays/gpt-4/language_level/language_level_2.out'

df = pd.read_csv(fname, sep=';')

df['role_object'] = df['role_object'].apply(json.loads)
df['chat'] = df['chat'].apply(json.loads)


for chat in df.iloc[0:]['chat'] :
    for m_idx in range(2, len(chat)):
        print(chat[m_idx]['content'])
        print('...')
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')
