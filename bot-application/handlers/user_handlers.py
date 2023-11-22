from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.keyboards import keyboard_start
from keyboards.inlinekeyboard import inline_keyboards, process_confirm
from database.db import add_client, add_message, give_message, reboot_del_message, \
    give_date_messages, db_application, give_application, clear_application, insert_application
from fsm.fsm import FSMApplicationBuy, FSMApplicationSell, give_next_state, start_fsm
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from config_data.config import load_config, Config
from lexicon.tools import for_admin

router = Router()
config: Config = load_config()


@router.message(Command(commands=['start', 'help']))
async def start_help(message: Message):
    await add_client(message.from_user.id)
    await clear_application(message.from_user.id)
    await reboot_del_message(message)
    # await message.bot.delete_message(message.chat.id, await give_message(message.from_user.id))
    await message.delete()
    send_message = await message.answer(text=LEXICON[message.text],
                                        reply_markup=await keyboard_start(message.text))
    await add_message(message.from_user.id, send_message.message_id, send_message.date)
    await give_date_messages()


# Разветвление на покупку или продажу ООО
@router.message(F.text.in_(['Покупка ООО', 'Продажа ООО']))
async def buying(message: Message, state: FSMContext):
    await start_fsm(state, message.text)
    # await state.set_state(FSMApplicationBuy.buy_firm)
    await message.bot.delete_message(message.chat.id, await give_message(message.from_user.id))
    await message.delete()
    send_message = await message.answer(text=LEXICON[await state.get_state()],
                                        reply_markup=await inline_keyboards('application'))
    await add_message(message.from_user.id, send_message.message_id, send_message.date)


# Вход в процесс создания заявки
@router.callback_query(F.data == 'create_application')
async def create_application(callback: CallbackQuery, state: FSMContext):
    await give_next_state(state)
    send_message = callback.message.edit_text(text=LEXICON[await state.get_state()][0])
    await add_message(callback.from_user.id, send_message.message_id)
    await send_message
    s = await state.get_state()
    # await state.set_state(FSMApplicationBuy.ask_region)
    # await clear_application(callback.from_user.id)


# Обработка возвращения в главное меню
@router.callback_query(F.data == 'main_menu')
async def back_main_menu(callback: CallbackQuery, state: FSMContext):
    send_message = await callback.message.answer(text=LEXICON[callback.data],
                                                 reply_markup=await keyboard_start('/start'))
    await add_message(callback.from_user.id, send_message.message_id, send_message.date)
    await callback.message.delete()
    await state.clear()


# Завершение заявки
@router.message(StateFilter(FSMApplicationBuy.ask_system, FSMApplicationSell.ask_cost))
async def check_application(message: Message, state: FSMContext):
    await db_application(message, state)
    await give_next_state(state)
    await message.bot.delete_message(message.chat.id, await give_message(message.from_user.id))
    await message.delete()
    send_message = await message.answer(text=f'<b>Ваша заявка:</b>\n\n{await give_application(message.from_user.id)}',
                                        reply_markup=await process_confirm(message.text))
    await add_message(message.from_user.id, send_message.message_id, send_message.date)
    print(await give_application(message.from_user.id))


@router.message(~StateFilter(default_state, FSMApplicationBuy.buy_firm, FSMApplicationSell.sell_firm))
async def write_application(message: Message, state: FSMContext):
    await db_application(message, state)
    await give_next_state(state)
    await message.bot.delete_message(message.chat.id, await give_message(message.from_user.id))
    await message.delete()
    send_message = await message.answer(text=LEXICON[await state.get_state()][0])
    await add_message(message.from_user.id, send_message.message_id, send_message.date)


# отмена заявки
@router.callback_query(F.data == 'cancel_application')
async def cancel_application(callback: CallbackQuery, state: FSMContext):
    send_message = await callback.message.edit_text(text=LEXICON[await state.get_state()],
                                                    reply_markup=await inline_keyboards('application'))
    await add_message(callback.from_user.id, send_message.message_id, send_message.date)
    await clear_application(callback.from_user.id)
    await start_fsm(state)



# await message.answer(text=f"<b><a href='tg://user?id={2141923788}'>Связаться</a></b>")
# заявка оформлена
@router.callback_query(F.data == 'confirm_application')
async def confirm_application(callback: CallbackQuery, state: FSMContext):
    send_message = await callback.message.edit_text(text=LEXICON[callback.data],
                                                    reply_markup=await inline_keyboards('application'))
    await add_message(callback.from_user.id, send_message.message_id)
    send_message = await callback.bot.send_message(config.admin.id, text=await for_admin(callback.bot,
                                                                                         callback.from_user.id),
                                                   reply_markup=await inline_keyboards('confirm_application',
                                                                                       callback.from_user.id))
    await insert_application(send_message.message_id, send_message.text, send_message.date)
    await clear_application(callback.from_user.id)


# удаление любого сообщения от пользователя
@router.message()
async def del_any_message(message: Message):
    await message.answer(text=str(message.chat.id))
    await message.delete()
