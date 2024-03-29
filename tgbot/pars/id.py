
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from loader import driver_loader


async def id_input(id):
    driver = driver_loader.name()

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

async def id_call(id):
    await id_input(id=id)