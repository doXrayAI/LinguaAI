
import pandas as pd
import json

fname = 'db/messages.csv'

# Returns persisted chat contexts
def load_chat_ids_and_context(fname=fname):
    
    chats = pd.read_csv(fname, sep=';', dtype={'id': str})
    chats['role_object'] = chats['role_object'].apply(json.loads)
    
    return chats[['id','role_object', 'language', 'language_level' ]]

# Perists new chat on disk
# Returns the new chat object
def persist_new_chat(language, language_level, setting, GPT_role, user_role, chat_messages):
    
    chats = pd.read_csv(fname, sep=';', dtype={'id': str})
    id = len(chats)
    
    role_object = {'setting': setting,
                   'GPT_role': GPT_role,
                   'user_role': user_role,
                   'roles': [GPT_role, user_role]}
    
    new_chat =  pd.DataFrame(data=[{
        'id': id,
        'language': language,
        'language_level': language_level,
        'role_object' : role_object,
        'chat' : chat_messages
        }]
    )
    
    new_chat_return = new_chat.copy(deep=True)
    new_chat['role_object'] = new_chat['role_object'].apply(json.dumps)
    new_chat['chat'] = new_chat['chat'].apply(json.dumps)
    
    chats = pd.concat([chats, new_chat])
    
    chats.to_csv(fname, sep=';', index=False, header=True)
    
    return new_chat_return


    
# Returns persisted chat object and messages with a given id    
def load_chat_messages(id):
    df = pd.read_csv(fname, sep=';', dtype={'id': str})
    df['role_object'] = df['role_object'].apply(json.loads)
    df['chat'] = df['chat'].apply(json.loads)

    return df[df['id']== id]
    

# Persists updated chat messages 
# Returns the updated chat object
def persist_updated_chat(chat_id, updated_chat_messages):
        
    chats = pd.read_csv(fname, sep=';', dtype={'id': str})
    chats.loc[int(chat_id), 'chat'] = json.dumps(updated_chat_messages)    

    chats.to_csv(fname, sep=';', index=False, header=True)
    
    chats['role_object'] = chats['role_object'].apply(json.loads)
    chats['chat'] = chats['chat'].apply(json.loads)
    
    return chats[chats['id']== chat_id]
    