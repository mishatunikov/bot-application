from database.db import give_application
from lexicon.lexicon import LEXICON
from aiogram import Bot
from random import choice


async def for_admin(bot: Bot, user_id: int, state: str):
    user_info = await bot.get_chat(user_id)
    if user_info.has_private_forwards:
        link = f'{choice("🤠👻👨👮‍♂️👨‍🍳👼🫃🙂🦧")}<b>Профиль клиента</b> - <b>@{user_info.username}</b>✈️' \
            if user_info.username else f'{choice("🤠👻👨👮‍♂️👨‍🍳👼🫃🙂🦧")}<b>Профиль клиента</b> - tg://user?id={user_id}'
        return '{}{}\n\n{}'.format(LEXICON[state][1],
                                   link,
                                   await give_application(user_id))
    return '{}{}\n\n{}'.format(LEXICON[state][1],
                               f"{choice('🤠👻👨👮‍♂️👨‍🍳👼🫃🙂🦧')}<b><a href='tg://user?id={user_id}'>"
                               f"Профиль клиента</a></b>✈️",
                               await give_application(user_id))
