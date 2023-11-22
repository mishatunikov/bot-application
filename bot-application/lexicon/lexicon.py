LEXICON = {'/start': 'Добро пожаловать!\n'
                     'Выберите интересующее направление.',
           '/help': 'Вы можете оставить свою завку здесь',
           'FSMApplicationBuy:buy_firm': 'Здесь вы можете создать заявку на покупку ООО',
           'main_menu': 'Вы вернулись в главное меню!\nВыберите интересующее направление.',
           'application': 'Опишите фирму',
           'confirm_application': '<b>Ваша заявка принята!🎉</b>\nВ ближайшее время менеджер свяжется с вами',
           'FSMApplicationBuy:ask_region': ('Какие регионы вас интересуют?',
                                            '<i><b>1. Рассматриваемые регионы:</b></i>'),
           'FSMApplicationBuy:ask_age': ('Введите минимальные возраст фирмы.',
                                         '\n\n<i><b>2. Минимальный ворзрат фирмы:</b></i>'),
           'FSMApplicationBuy:ask_rmp': ('Требуются ли обороты?\n\nЕсли да, то за какой период?',
                                         '\n\n<i><b>3. Необходимость оборотов:</b></i>'),
           'FSMApplicationBuy:ask_system': ('Какая система налогообложения интересует?',
                                            '\n\n<i><b>4. Система налогообложения</b>:</i>'),
           'FSMApplicationSell:sell_firm': 'Здесь вы можете создать заявку на продажу ООО',
           'FSMApplicationSell:ask_id_firm': ('Введите ИНН.', '<i><b>1. ИНН:</b></i>'),
           'FSMApplicationSell:ask_about_bills': ('Подскажите, в каких банках открыты счета?',
                                                  '\n\n<i><b>2. Открытые счета:</b></i>'),
           'FSMApplicationSell:ask_system': ('Какая система налогооблажения используется в данный момент?',
                                             '\n\n<b><i>3. Система налогообложения:</i></b>'),
           'FSMApplicationSell:ask_rmp': ('Имеются ли обороты за текущий год?',
                                          '\n\n<b><i>4. Обороты за текущий год:</i></b>'),
           'FSMApplicationSell:ask_cost': ('Укажите стоимость фирмы (₽)',
                                           '\n\n<b><i>4. Стоимость(₽):</i></b>'),
           'send': '🆕<b>Новая заявка!</b>🆕\n\n'}

MAIN_MENU_COMMAND = {
    'start': 'Начать',
    'help': 'Справка'
}


KEYBOARDS = {
    '/start': ['Покупка ООО', 'Продажа ООО'],
    'application': {'Создать заявку': 'create_application', 'Назад': 'main_menu'},
    'confirm_cancel': {'❌': 'cancel_application', '✅': 'confirm_application'},
    'cancel_creating': {'отмена': 'cancel_application'},
    'confirm_application': {'Заявка обработана✅': 'close_application'}
}

