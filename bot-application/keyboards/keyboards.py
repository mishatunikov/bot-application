from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonRequestUser
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import KEYBOARDS


async def keyboard_start(command) -> ReplyKeyboardMarkup | ReplyKeyboardRemove:
    if command in KEYBOARDS:
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.add(*[KeyboardButton(text=i)
                         for i in KEYBOARDS[command]])
        return kb_builder.as_markup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    input_field_placeholder='Используйте кнопки')
    return ReplyKeyboardRemove()
