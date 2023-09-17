from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import lexicon_ru

button_yes: KeyboardButton = KeyboardButton(text=lexicon_ru['button_yes'])
button_no: KeyboardButton = KeyboardButton(text=lexicon_ru['button_no'])
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb_builder.row(button_yes, button_no, width=2)
yes_no_kb: ReplyKeyboardMarkup = kb_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True)

button_1: KeyboardButton = KeyboardButton(text=lexicon_ru['rock'])
button_2: KeyboardButton = KeyboardButton(text=lexicon_ru['paper'])
button_3: KeyboardButton = KeyboardButton(text=lexicon_ru['scissors'])
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3]], resize_keyboard=True)
