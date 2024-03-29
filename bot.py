import asyncio
import logging

from loader import logger, bot, dp
from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.ActivationCodes.acivation_code import register_activation_code
from tgbot.handlers.ActivationCodes.codes.register_120 import register_120
from tgbot.handlers.ActivationCodes.codes.register_180 import register_180
from tgbot.handlers.ActivationCodes.codes.register_300 import register_300
from tgbot.handlers.ActivationCodes.codes.register_60 import register_60
from tgbot.handlers.ActivationCodes.codes.resgister_325 import register_325
from tgbot.handlers.AddAccount import register_added_account
from tgbot.handlers.Show_Note import register_show_note
from tgbot.handlers.admin import register_admin
from tgbot.handlers.dell_true import register_del_true
from tgbot.handlers.echo import register_echo
from tgbot.handlers.run_browser import register_run_browser
from tgbot.handlers.user import register_user
from tgbot.middlewares.environment import EnvironmentMiddleware


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_activation_code(dp)
    register_60(dp)
    register_120(dp)
    register_180(dp)
    register_300(dp)
    register_325(dp)
    register_added_account(dp)
    register_show_note(dp)
    register_del_true(dp)
    register_run_browser(dp)

    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")


    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
