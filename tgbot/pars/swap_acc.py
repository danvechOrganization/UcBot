import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from loader import driver_loader, bot
from tgbot.services.Counter.counter import Counter
from tgbot.services.Database.sqlite import Database
from tgbot.services.chromiumdriver import proxy_run


async def swap_acc(id):

    await proxy_run()
    driver = driver_loader.name()
    db = Database("tgbot/services/Database/codes.db")
    account_and_password = db.execute(
        f"SELECT login, pass FROM ACCOUNTS ORDER BY id ASC LIMIT 1 OFFSET {Counter.COUNTER}", fetchone=True)

    # Wait for the login button to be clickable
    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='login'] a")))
    # Click on the login button
    element.click()

    # Switch to the login iframe
    driver.switch_to.frame('login-iframe')

    # Find email input field and enter email
    email_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Enter email to sign in or sign up']")))
    email_input.send_keys(f'{account_and_password[0]}')

    time.sleep(1)

    # Click on the confirm button after entering email
    confirm_email_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn.comfirm-btn")))
    confirm_email_button.click()

    # Find password input field and enter password
    password_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter password']")))
    password_input.send_keys(f'{account_and_password[1]}')

    # Click on the confirm button after entering password
    confirm_password_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn.comfirm-btn")))
    confirm_password_button.click()

    # Переход в раздел пабга
    confirm_password_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "a[title='PUBG MOBILE'] span[class='btn']")))
    confirm_password_button.click()

    # Ждем, пока загрузится весь контент страницы
    iframe_src = "https://www.midasbuy.com/act/pagedoo/Activity_1708915779_BZUYCT/pc/index.html?from=&lan=en&country=bd"
    iframe = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, f'iframe[src="{iframe_src}"]')))
    driver.switch_to.frame(iframe)
    last_element = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "(//span[contains(text(),'You have a reward worth 10620UC~34620UC to be unlo')])[1]")))

    # Перезагрузка вкладки
    driver.refresh()

    # Переход в раздел кодов
    confirm_password_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                          "a[data-iformat='buy'] div p")))
    confirm_password_button.click()

    # Клик на кнопку ввода ID
    switch_id = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                            "i[class='i-midas:switch icon ']")))
    switch_id.click()

    # Очистка поля id
    password_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter Player ID']")))
    password_input.clear()

    # Ввод в поле
    password_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter Player ID']")))
    password_input.send_keys(f'{id}')

    # Клик на ОК
    confirm_password_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'OK')])[2]")))
    confirm_password_button.click()

    await bot.send_message(5321109924, f"Я сменил аккаунт на {account_and_password[0]}")


async def acc_call(id):
    await swap_acc(id=id)