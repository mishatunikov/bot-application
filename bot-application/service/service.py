import asyncio
from fsm.fsm import FSMApplicationBuy, FSMApplicationSell, FSMContext
from datetime import datetime, timedelta
from database.db import give_old_message, clear_old_message
from aiogram import Bot


async def delete_old_messages(bot: Bot):
    """Checking old message"""
    # k = await give_old_message(current_time.timestamp())
    while True:
        print(await give_old_message(datetime.now().timestamp()))
        for i, j in await give_old_message(datetime.now().timestamp()):
            print(i, j)
            # await bot.send_message(chat_id=i, text=f'Сообщение устарело - {j}')
            await bot.delete_message(chat_id=i, message_id=j)
            await clear_old_message(j)
        await asyncio.sleep(3600)







