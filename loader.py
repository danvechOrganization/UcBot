import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.services.Drivers.drivers import Drivers

driver_loader = Drivers()
config = load_config(".env")
logger = logging.getLogger(__name__)
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
dp = Dispatcher(bot, storage=storage)