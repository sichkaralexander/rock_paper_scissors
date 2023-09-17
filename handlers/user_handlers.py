from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import yes_no_kb, game_kb
from services.services import get_bot_choice, winner
from lexicon.lexicon import lexicon_ru
router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=lexicon_ru['start'], reply_markup=yes_no_kb)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_ru['help'], reply_markup=yes_no_kb)


@router.message(F.text == lexicon_ru['button_yes'])
async def yes(message: Message):
    await message.answer(text=lexicon_ru['yes'], reply_markup=game_kb)


@router.message(F.text == lexicon_ru['button_no'])
async def no(message: Message):
    await message.answer(text=lexicon_ru['no'])


@router.message(F.text .in_([lexicon_ru['rock'], lexicon_ru['paper'], lexicon_ru['scissors']]))
async def botchoice(message: Message):
    lexicon_ru['user_choice'] = message.text
    lexicon_ru['bot_choice'] = get_bot_choice()

    await message.answer(text=f'вы выбрали - {lexicon_ru["user_choice"]} - мой выбор - {lexicon_ru["bot_choice"] }, -, {winner()} ')
    await message.answer(text = 'Хочешь поиграть ещё раз?',reply_markup = yes_no_kb)