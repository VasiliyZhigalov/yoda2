from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def search_shopping_list_kb_inline():
    search_btn = InlineKeyboardButton(text="Найти товары", callback_data = 'search_btn')
    add_btn = InlineKeyboardButton(text="Добавить товар ", callback_data='add_btn')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[search_btn, add_btn]])
    return keyboard
