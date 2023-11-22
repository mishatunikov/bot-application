import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from keyboards.set_menu import set_main_menu
from handlers import user_handlers, admin_handlers
from database import db
from fsm.fsm import storage
from service.service import delete_old_messages

import logging
logger = logging.getLogger()


async def main() -> None:
    # Подключаем базу данных
    await db.db_start()
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting Bot')
    dp = Dispatcher(storage=storage)

    config: Config = load_config()
    bot = Bot(token=config.bot.token, parse_mode='html')
    await set_main_menu(bot)

    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)

    asyncio.create_task(delete_old_messages(bot))

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
