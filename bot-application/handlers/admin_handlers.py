from aiogram import Router, F
from config_data.config import load_config
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from database.db import application_processed

router = Router()
#
router.message.filter(F.from_user.id == int(load_config().admin.id))
router.callback_query.filter(F.from_user.id == int(load_config().admin.id))


@router.message(CommandStart())
async def start(message: Message):
    send_message = await message.answer(text='Admin')
    await message.delete()


@router.callback_query(F.data == 'close_application')
async def close_application(callback: CallbackQuery):
    await callback.message.edit_reply_markup()
    s = callback.message.message_id
    await application_processed(s)
    await callback.message.delete()
