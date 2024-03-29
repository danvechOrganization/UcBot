import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from loader import driver_loader
from tgbot.pars.swap_acc import acc_call
from tgbot.services.Counter.counter import Counter


async def code_insert(code, id):
    driver = driver_loader.name()

    # Очистка поля кода
    cleer_code = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Please enter a redeem code']")))
    cleer_code.clear()

    # Ввод в поле кода
    insert_code = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Please enter a redeem code']")))
    insert_code.send_keys(f'{code}')

    time.sleep(1)

    # Клик на ок Кода
    click_ok = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'OK')])[2]")))
    click_ok.click()

    # Клик нажатие Submit
    click_submit = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'Submit')])[1]")))
    click_submit.click()

    try:
        # Клик на ОК после подтверждения
        click_ok_verif = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'OK')])[3]")))
        click_ok_verif.click()

        # Перезагрузка вкладки
        driver.refresh()

        return False
    except:
        try:
            verify_button = WebDriverWait(driver, 5).until(
                ec.visibility_of_element_located((By.XPATH, "(//div[contains(text(),'verify comfirm')])[1]")))
            await acc_call(id)
            Counter.add_counter()
            return True
        except:
            verify_win = WebDriverWait(driver, 5).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, "#tcaptcha_iframe_dy")))
            await acc_call(id)
            Counter.add_counter()
            return True


async def code_call(code, id):
    success = await code_insert(code=code, id=id)
    if success:
        return True
    else:
        return False
