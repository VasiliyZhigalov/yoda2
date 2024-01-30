import asyncio
import logging
from aiogram import Bot, Dispatcher
from src import config
from src.handlers import shopping_list

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher(bot=bot)
dp.include_routers(shopping_list.router)

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        pass
