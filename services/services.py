import random
from lexicon.lexicon import lexicon_ru


def get_bot_choice():
    return random.choice(['камень', 'бумага', 'ножницы'])


def winner():
    if lexicon_ru['bot_choice']== lexicon_ru['user_choice']:
        return lexicon_ru['winner']
    elif lexicon_ru['bot_choice'] == 'камень' and lexicon_ru['user_choice']== 'ножницы':
        return lexicon_ru['winner_1'] 
    elif lexicon_ru['bot_choice'] == 'бумага' and lexicon_ru['user_choice'] == 'камень':
       return lexicon_ru['winner_1'] 
    elif lexicon_ru['bot_choice'] == 'ножницы' and lexicon_ru['user_choice'] == 'бумага':
        return lexicon_ru['winner_1'] 
    else:
        return lexicon_ru['winner_2']
