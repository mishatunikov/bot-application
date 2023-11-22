from aiogram.types import BotCommand
from aiogram import Bot

from lexicon.lexicon import MAIN_MENU_COMMAND


def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command,
                   description=description)
        for command, description in MAIN_MENU_COMMAND.items()
    ]
    return bot.set_my_commands(main_menu_commands)