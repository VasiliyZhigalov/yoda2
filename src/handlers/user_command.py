from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    chat = message.chat
    current_user = user.read_user(chat.id)
    if current_user is None:
        current_user = user.create_user(chat.id, chat.username)
    await message.answer(f"Приветсвую тебя, {current_user.name}!")
