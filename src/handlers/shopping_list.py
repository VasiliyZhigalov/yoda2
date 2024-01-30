from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.keyboards.shopping_list_kbs import search_shopping_list_kb_inline
from src.services.shopping_list_service import ShoppingListService

from src.states import AddingProductsToList

router = Router()


@router.message(StateFilter(None), Command("shopping_list"))
async def shopping_list_command(message: Message, state: FSMContext):
    await message.answer("(удалил старый список покупок)\n"
                         "Внесите список покупок в формате:\n"
                         "Товар1 - 1 кг\n"
                         "Товар2 - n шт.")
    await state.set_state(AddingProductsToList.adding_product)


@router.message(StateFilter(AddingProductsToList.adding_product), F.text.contains('-'))
async def adding_product(message: Message, state: FSMContext):
    shl_service = ShoppingListService()
    queries = shl_service.save_user_queries(message.text, message.chat.id)
    str1 = ''
    for q in queries:
        str1 += q.product + " - " + str(q.quantity) + " " + q.unit + "\n"
    await message.answer("Ваш список покупок:\n" + str1, reply_markup=search_shopping_list_kb_inline())


@router.message(StateFilter(AddingProductsToList.adding_product))
async def adding_product(message: Message, state: FSMContext):
    await message.answer("Вы ввели товары не верном формате, порпобуйте так:\n"
                         "Товар1 - 1 кг\n"
                         "Товар2 - n шт.")


@router.callback_query(StateFilter(AddingProductsToList.adding_product), F.data.in_(['search_btn']))
async def search_product(callback: CallbackQuery):
    await callback.answer("Пожалуйста, подождите, поиск может занять несколько минут")
    shl_service = ShoppingListService()
    prods = shl_service.get_products_by_user_queries(user_id=callback.message.chat.id)
    str1 = ''
    for p in prods:
        str1 += p.title + ":" + p.price + "\n"
    callback.message.answer("str1")
