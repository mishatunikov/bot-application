LEXICON = {'/start': 'Добро пожаловать!\n'
                     'Выберите интересующее направление.',
           '/help': 'С помощью нашего верного бота-помошника вы в любое время можете '
                    'оставить заявку на интересующее вас направление. \n\nНачать - \start😊',
           'FSMApplicationBuy:buy_firm': ('Здесь вы можете создать заявку на покупку ООО',
                                          '<b>🆕Новая заявка на <u>покупку</u>!</b>🆕\n\n'),
           'main_menu': 'Вы вернулись в главное меню!\nВыберите интересующее направление.',
           'application': 'Опишите фирму',
           'confirm_application': '<b>Ваша заявка принята!🎉</b>\nВ ближайшее время менеджер свяжется с вами',
           'FSMApplicationBuy:ask_region': ('Какие регионы вас интересуют?',
                                            '1. Рассматриваемые регионы:'),
           'FSMApplicationBuy:ask_age': ('Введите минимальные возраст фирмы.',
                                         '\n\n2. Минимальный возраст фирмы:'),
           'FSMApplicationBuy:ask_rmp': ('Требуются ли обороты?\n\nЕсли да, то за какой период?',
                                         '\n\n3. Необходимость оборотов:'),
           'FSMApplicationBuy:ask_system': ('Какая система налогообложения интересует?',
                                            '\n\n4. Система налогообложения:'),
           'FSMApplicationSell:sell_firm': ('Здесь вы можете создать заявку на продажу ООО',
                                            '<b>🆕Новая заявка на <u>продажу</u>🆕</b>\n\n'),
           'FSMApplicationSell:ask_id_firm': ('Введите ИНН вашей фирмы.', '1. ИНН:'),
           'FSMApplicationSell:ask_about_bills': ('Подскажите, в каких банках открыты счета?',
                                                  '\n\n2. Открытые счета:'),
           'FSMApplicationSell:ask_system': ('Какая система налогооблажения используется в данный момент?',
                                             '\n\n3. Система налогообложения:'),
           'FSMApplicationSell:ask_rmp': ('Имеются ли обороты за текущий год?',
                                          '\n\n4. Обороты за текущий год:'),
           'FSMApplicationSell:ask_cost': ('Укажите стоимость фирмы (<b>₽</b>)',
                                           '\n\n4. Стоимость(<b>₽</b>):'),
           'not_sub': 'Для использования бота подпишись на канал 😉.'}

MAIN_MENU_COMMAND = {
    'start': 'Начать',
    'help': 'Справка'
}


KEYBOARDS = {
    '/start': ['Покупка ООО', 'Продажа ООО'],
    'application': {'Создать заявку': 'create_application', 'Назад': 'main_menu'},
    'confirm_cancel': {'❌': 'cancel_application', '✅': 'confirm_application'},
    'cancel_creating': {'отмена': 'cancel_application'},
    'confirm_application': {'Заявка обработана✅': 'close_application'},
    'not_sub': {'Подписаться': 'https://t.me/bsconsalt'}
}

