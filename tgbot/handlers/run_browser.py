from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.services.chromiumdriver import proxy_run


async def run_browser(message: Message):
    await proxy_run()



def register_run_browser(dp: Dispatcher):
    dp.register_message_handler(run_browser, text="Запуск Браузера")