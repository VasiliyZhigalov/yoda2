from aiogram.fsm.state import StatesGroup, State


class AddingProductsToList(StatesGroup):
    adding_product = State()
    search_product = State()
