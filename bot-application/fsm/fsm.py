from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.context import FSMContext

redis = Redis(host='localhost')
storage = RedisStorage(redis=redis)


class FSMApplicationBuy(StatesGroup):
    buy_firm = State()
    ask_region = State()
    ask_age = State()
    ask_rmp = State()
    ask_system = State()


class FSMApplicationSell(StatesGroup):
    sell_firm = State()
    ask_id_firm = State()
    ask_about_bills = State()
    ask_system = State()
    ask_rmp = State()
    ask_cost = State()


async def give_next_state(state: FSMContext):
    current_state = await state.get_state()
    states_group = eval(current_state.split(':')[0])
    state_index = states_group.__all_states__.index(await state.get_state())
    if state_index + 1 < len(states_group.__all_states__):
        await state.set_state(states_group.__all_states__[state_index + 1])
    elif state_index == len(states_group.__all_states__) - 1:
        await state.set_state(states_group.__all_states__[0])
    # else:
    #     await state.clear()


async def start_fsm(state: FSMContext, text: str = None):
    if text:
        await state.set_state([FSMApplicationBuy.buy_firm, FSMApplicationSell.sell_firm][text == 'Продажа ООО'])
    else:
        s = {'FSMApplicationBuy': FSMApplicationBuy.buy_firm, 'FSMApplicationSell': FSMApplicationSell.sell_firm}
        k = await state.get_state()
        await state.set_state(s[k.split(':')[0]])
