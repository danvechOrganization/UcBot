import asyncio
import random
from selenium import webdriver
import os

proxy_list = [
    '185.39.148.176:8000',
    '123.456.789.101:8080',
    # Добавьте здесь другие прокси-серверы по желанию
]

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
]

def get_chromedriver(proxy_list=None, user_agent_list=None):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    if proxy_list:
        proxy = random.sample(proxy_list, 1)[0]
        options.add_argument(f'--proxy-server={proxy}')

    if user_agent_list:
        user_agent = random.sample(user_agent_list, 1)[0]
        options.add_argument(f'--user-agent={user_agent}')

    driver = webdriver.Chrome(options=options)
    return driver

async def proxy_run():

    driver = get_chromedriver(proxy_list=proxy_list, user_agent_list=user_agent_list)
    driver.get('https://www.midasbuy.com/midasbuy/bd/redeem/pubgm')
    return driver
