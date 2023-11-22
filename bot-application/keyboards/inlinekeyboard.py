from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import KEYBOARDS


async def inline_keyboards(text: str, user_id: int = None) -> InlineKeyboardMarkup:
    ikb_builder = InlineKeyboardBuilder()
    # if user_id:
    #     ikb_builder.add(InlineKeyboardButton(text='Профиль клиента', url=f'tg://user?id={user_id}'))
    ikb_builder.row(*[InlineKeyboardButton(text=i, callback_data=j)
                      for i, j in KEYBOARDS[text].items()], width=1)
    return ikb_builder.as_markup()


async def process_confirm(text: str) -> InlineKeyboardMarkup:
    info = 'confirm_cancel' if text != 'create_application' else 'cancel_creating'
    ikb_builder = InlineKeyboardBuilder()
    ikb_builder.add(*[InlineKeyboardButton(text=i, callback_data=j)
                      for i, j in KEYBOARDS[info].items()])
    return ikb_builder.as_markup()


in_kb = InlineKeyboardBuilder()
in_kb.add(InlineKeyboardButton(text='here', url='tg://user?id=2141923788'))
