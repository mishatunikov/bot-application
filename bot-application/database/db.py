import sqlite3 as sq
from aiogram.types import Message
from datetime import datetime
from aiogram.fsm.context import FSMContext
from lexicon.lexicon import LEXICON

# Подключение базы, если нет файла, то создается.
db = sq.connect('tg.db')
# Курсор, выполняет основные функции
cur = db.cursor()


async def db_start():
    """Create db"""
    cur.execute("CREATE TABLE IF NOT EXISTS clients ("
                "tg_id INTEGER PRIMARY KEY,"
                "chat_id INTEGER,"
                "link TEXT,"
                "application TEXT,"
                "message_id INTEGER,"
                "time_message INTEGER)")

    cur.execute("CREATE TABLE IF NOT EXISTS active_applications ("
                "message_id INTEGER PRIMARY KEY,"
                "application TEXT,"
                "time_message INTEGER)")
    db.commit()


async def add_client(user_id: int):
    """Add client in db if not exist"""
    user = cur.execute("SELECT * FROM clients WHERE tg_id = ?", (user_id,)).fetchone()
    if not user:
        cur.execute('INSERT INTO clients (tg_id, link) VALUES (?, ?)', (user_id, f'tg://user?id={user_id}'))
    db.commit()


async def add_message(user_id: int, message_id: int, date: datetime = None):
    """Add last bot message in db"""
    if date:
        cur.execute('UPDATE clients SET message_id=?, time_message=? WHERE tg_id = ?',
                    (message_id, date.timestamp(), user_id))
    else:
        cur.execute('UPDATE clients SET message_id=? WHERE tg_id = ?',
                    (message_id, user_id))
    db.commit()


async def give_message(user_id: int):
    """Cen give last bot message_id"""
    return cur.execute('SELECT message_id FROM clients WHERE tg_id = ?', (user_id,)).fetchone()[0]


async def reboot_del_message(message: Message):
    """Del last bot message after command"""
    message_id = cur.execute('SELECT message_id FROM clients WHERE tg_id = ?', (message.from_user.id,)).fetchone()
    if message_id[0]:
        await message.bot.delete_message(message.chat.id, message_id[0])


async def give_date_messages():
    """Can give date of last bot message"""
    messages = cur.execute('SELECT message_id, time_message FROM clients WHERE time_message NOT NULL').fetchall()


async def db_application(message: Message, state: FSMContext):
    current_application = cur.execute('SELECT application FROM clients WHERE tg_id = ?',
                                      (message.from_user.id,)).fetchone()

    if current_application[0]:
        cur.execute('UPDATE clients SET application = application || ? WHERE tg_id = ?',
                    (f'{LEXICON[await state.get_state()][1]} {message.text}', message.from_user.id,))
    else:
        cur.execute('UPDATE clients SET application = ? WHERE tg_id = ?',
                    (f'{LEXICON[await state.get_state()][1]} {message.text}', message.from_user.id,))

    db.commit()


async def give_application(user_id: int) -> str:
    return cur.execute('SELECT application FROM clients WHERE tg_id = ?', (user_id,)).fetchone()[0]


async def clear_application(user_id: int):
    cur.execute('Update clients SET application = NULL WHERE tg_id = ?', (user_id,))
    db.commit()


# admin
async def insert_application(message_id: int, application_text: str, date: datetime):
    cur.execute('INSERT INTO active_applications (message_id, application, time_message)'
                'VALUES (?, ?, ?)', (message_id, application_text, date.timestamp()))
    db.commit()


async def application_processed(message_id: int):
    cur.execute('DELETE FROM active_applications WHERE message_id = ?', (message_id,))
    db.commit()


async def give_old_message(current_time):
    return cur.execute('SELECT tg_id, message_id FROM clients WHERE message_id is not NULL and '
                       '? - time_message > 47 * 3600', (current_time,)).fetchall()


async def clear_old_message(message_id: int):
    cur.execute('UPDATE clients SET message_id = NULL, time_message = NULL, application = NULL '
                'WHERE message_id = ?', (message_id,))
    db.commit()
