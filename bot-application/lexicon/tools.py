from database.db import give_application
from lexicon.lexicon import LEXICON
from aiogram import Bot


async def for_admin(bot: Bot, user_id: int):
    user_info = await bot.get_chat(user_id)
    if user_info.has_private_forwards:
        link = f'<b>Профиль клиента</b> - <b>@{user_info.username}</b>' if user_info.username \
            else f'<b>Профиль клиента</b> - tg://user?id={user_id}'
        return '{}{}\n\n{}'.format(LEXICON['send'],
                                   link,
                                   await give_application(user_id))
    return '{}{}\n\n{}'.format(LEXICON['send'],
                               f"<b><a href='tg://user?id={user_id}'>Профиль клиента</a></b>👨‍💻",
                               await give_application(user_id))
