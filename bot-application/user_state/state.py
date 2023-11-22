from aiogram.types import Message

# states = {'calculate': False}
db_clients = {}


def add_client_db(message: Message):
    db_clients.setdefault(message.from_user.id, {'application': False, 'process': '', 'delmessage_id': ''})


def application_on(user_id: int):
    db_clients[user_id]['application'] = True



def application_off(user_id: int):
    db_clients[user_id]['application'] = False


def activate_process(message: Message):
    db_clients[message.from_user.id]['process'] = message.text


def take_message(user_id: int, message_id: int):
    print(user_id, message_id)
    db_clients[user_id]['delmessage_id'] = message_id
    print(db_clients)



