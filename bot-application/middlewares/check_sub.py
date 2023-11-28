from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from keyboards.inlinekeyboard import subscribe
from database.db import add_message, give_message, add_client


class CheckSubscription(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[[Message], Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member(chat_id='@bsconsalt',
                                                      user_id=event.from_user.id)
        await add_client(event.from_user.id)
        if chat_member.status == 'left':
            old_message = await give_message(event.from_user.id)
            if old_message:
                await event.bot.delete_message(chat_id=event.from_user.id, message_id=old_message)
            send_message = await event.answer(text=LEXICON['not_sub'],
                                              reply_markup=await subscribe())
            await event.delete()
            await add_message(send_message.chat.id, send_message.message_id, send_message.date)
        else:
            return await handler(event, data)
