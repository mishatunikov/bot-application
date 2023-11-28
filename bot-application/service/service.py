import asyncio
from keyboards.inlinekeyboard import inline_keyboards
from datetime import datetime
from database.db import give_old_message, clear_old_message, give_old_application, refresh_application
from aiogram import Bot
from config_data.config import load_config, Config

config: Config = load_config()


async def delete_old_messages(bot: Bot):
    """Checking old message and application"""
    while True:
        for i, j in await give_old_message(datetime.now().timestamp()):
            # await bot.send_message(chat_id=i, text=f'Сообщение устарело - {j}')
            await bot.delete_message(chat_id=i, message_id=j)
            await clear_old_message(j)

        for message_id, time_message, application in await give_old_application(datetime.now().timestamp()):
            await bot.delete_message(chat_id=config.admin.id, message_id=message_id)
            send_message = await bot.send_message(chat_id=config.admin.id, text=application,
                                                  reply_markup=await inline_keyboards('confirm_application'))
            await refresh_application(send_message.message_id, send_message.date.timestamp(), message_id)

        await asyncio.sleep(3600)
