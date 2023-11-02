import src.cli as cli
import src.plays.play as bot_play
from src.bot_pipeline import identity_pipeline, make_bot_pipeline
from src.bots.refinement_bot import LanguageLevelRefinementBot, RoleFitnessLanguageLevelBot

if __name__ == "__main__":
    #cli.chat_initiation()
    
    example = {
        'setting': 'In a library',
        'GPT_role': 'Librarian',
        'user_role': 'Visitor'
    }
    
    language = 'English'
    language_level = 'B2'
    
    ll_bot = LanguageLevelRefinementBot(language_level)
    rf_ll_bot = RoleFitnessLanguageLevelBot(example['GPT_role'], example['user_role'], language_level)
    
    pipeline = identity_pipeline
    #pipeline = make_bot_pipeline([rf_ll_bot.send,])
    
    chat = bot_play.play(example['setting'], example['GPT_role'], example['user_role'], language, language_level, pipeline, 3)
    
    for c in chat:
        print(c['content'])
        print()
    