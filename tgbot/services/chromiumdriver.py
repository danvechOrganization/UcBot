import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loader import driver_loader, bot
from tgbot.services.ProxyAndUA.proxy_list import proxy_list
from tgbot.services.ProxyAndUA.ua_list import user_agent_list

previous_proxy = None  # Переменная для хранения предыдущего прокси
previous_driver = None # Переменная для хранения предыдущего драйвера

def get_chromedriver(proxy_list=None, user_agent_list=None):
    global previous_proxy  # Объявление глобальной переменной
    global previous_driver
    # Создаем объект опций Chrome и отключаем загрузку изображений
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    # Добавляем опцию для отделения драйвера
    options.add_experimental_option("detach", True)

    #На весь экран
    options.add_argument("--start-maximized")
    #В фоне
    #options.add_argument("--headless")

    if proxy_list:
        # Удаляем предыдущий прокси из списка
        if previous_proxy in proxy_list:
            proxy_list.remove(previous_proxy)
        # Если все прокси были использованы, сбрасываем список
        if len(proxy_list) == 0:
            proxy_list = [
                '185.39.148.176:8000',
                '185.39.148.222:8000',
                '46.161.20.122:8000',
                '46.161.21.139:8000',
                '46.161.21.242:8000',
                '46.161.21.218:8000',
                '46.161.20.148:8000',
            ]
        # Выбираем новый прокси случайным образом
        proxy = random.sample(proxy_list, 1)[0]
        previous_proxy = proxy  # Обновляем значение previous_proxy
        options.add_argument(f'--proxy-server={proxy}')

    if user_agent_list:
        user_agent = random.sample(user_agent_list, 1)[0]
        options.add_argument(f'--user-agent={user_agent}')

    if previous_driver:
        try:
            previous_driver.quit()
        except Exception as e:
            print(f"An error occurred while quitting the previous Drivers: {e}")

        # Создаем новый драйвер
    driver = webdriver.Chrome(options=options)
    previous_driver = driver  # Сохраняем ссылку на новый драйвер
    print(previous_driver)
    return driver

async def proxy_run():
    global previous_driver
    driver = get_chromedriver(proxy_list=proxy_list, user_agent_list=user_agent_list)
    driver.get('https://www.midasbuy.com/midasbuy/bd/')
    driver_loader.set_name(driver)
    await bot.send_message(5321109924, "Браузер запущен")
    return driver
