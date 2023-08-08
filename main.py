import src.cli as cli
import src.plays.play as bot_play
from src.bot_pipeline import identity_pipeline

if __name__ == "__main__":
    #cli.chat_initiation()
    
    example = {
        'setting': 'In a library',
        'GPT_role': 'Librarian',
        'user_role': 'Visitor'
    }
    
    language = 'English'
    language_level = 'A2'
    
    chat = bot_play.play(example['setting'], example['GPT_role'], example['user_role'], language, language_level, identity_pipeline)
    
    for c in chat:
        print(c.content)
        print()
    