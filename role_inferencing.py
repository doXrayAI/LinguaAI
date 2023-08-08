import pandas as pd
from src.bots.role_inference_bot import RoleInferenceBot


fname = 'src/plays/settings.in'

lines = None
with open(fname) as f:
    lines = [ i.strip() for i in f.readlines()]
    
bot = RoleInferenceBot()

rez = []


for l in lines:
    inference = bot.send((l.strip(),))
    rez.append(inference)
    
    


df = pd.DataFrame({'setting': lines, 'role_object': rez})

df.to_csv('roles.out', index=False)