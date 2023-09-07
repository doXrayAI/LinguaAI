
import pandas as pd
import json

fname = 'db/messages.csv'


def load_chat_ids_and_context(fname=fname):
    
    chats = pd.read_csv(fname, sep=';')
    chats['role_object'] = chats['role_object'].apply(json.loads)
    
    return chats[['id','role_object', 'language', 'language_level' ]].to_dict('records')


def persist_new_chat(id, language, language_level, setting, GPT_role, user_role, chat):
    role_object = {'setting': setting,
                   'GPT_role': GPT_role,
                   'user_role': user_role,
                   'roles': [GPT_role, user_role]}
    
    new_chat =  pd.DataFrame(data=[{
        'id': id,
        'language': language,
        'language_level': language_level,
        'role_object' : role_object,
        'chat' : chat
        }]
    )
    
    new_chat['role_object'] = new_chat['role_object'].apply(json.dumps)
    new_chat['chat'] = new_chat['chat'].apply(json.dumps)
    
    new_chat.to_csv(fname, sep=';', mode='a', index=False, header=False)
    return new_chat.to_dict('records')
    
    
def load_chat_messages(id):
    
    df = pd.read_csv(fname, sep=';', dtype={'id': str})
    df['role_object'] = df['role_object'].apply(json.loads)
    df['chat'] = df['chat'].apply(json.loads)

    return df[df['id']== id].to_dict('records')