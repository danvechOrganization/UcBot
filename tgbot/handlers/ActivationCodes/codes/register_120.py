import sqlite3

import pyautogui
import pyperclip
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc import InputId_120
from tgbot.services.Counter.counter import Counter
from tgbot.services.Database.sqlite import Database
from tgbot.services.chromiumdriver import proxy_run


async def press_button_120(message: Message):
    photo = "tgbot/screenshots/Smena.png"
    try:
        photo_id = pyautogui.locateOnScreen(photo, confidence=0.8)
        pyautogui.click(photo_id, duration=0.25)
        pyautogui.sleep(2)
        await message.answer("Введите ID")
        await InputId_120.Id.set()
    except:
        await message.answer("Не нашел изображение")


async def answer_id_120(message: Message, state: FSMContext):
    id = message.text
    await message.answer(f"Круто, ты ввел {id}")
    await state.finish()
    pyperclip.copy(id)
    pyautogui.click(952, 368, duration=0.25)
    pyautogui.click(1141, 371, duration=0.25)
    pyautogui.click(936, 370, button='right', duration=0.25)
    pyautogui.sleep(1)
    pyautogui.click(991, 551, duration=0.25)
    pyautogui.click(968, 511, duration=0.25)
    pyautogui.sleep(2)

    for i in range(2):
        while True:
            # Извлекаем первый код из базы данных
            conn = sqlite3.connect("tgbot/services/Database/codes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT code FROM CODES WHERE IsUse = False LIMIT 1")
            code = cursor.fetchone()
            conn.commit()
            cursor.close()
            conn.close()

            # Если код существует, копируем его и удаляем из базы данных
            if code:
                pyperclip.copy(code[0])
                pyautogui.sleep(3)
                pyautogui.click(851, 691, duration=0.25)
                pyautogui.click(1070, 693, duration=0.25)
                pyautogui.click(867, 690, button='right', duration=0.25)
                pyautogui.sleep(1)
                pyautogui.click(936, 824, duration=0.25)
                pyautogui.click(1195, 691, duration=0.25)
                pyautogui.sleep(3)
                # Нажатие на Submit перед капчей
                pyautogui.click(946, 803, duration=0.25)
                pyautogui.sleep(3)
                # Проверяем, есть ли на экране кнопка "Я не робот"
                try:
                    pyautogui.locateOnScreen('tgbot/screenshots/Captcha.png', confidence=0.9)
                    # Копируем аккаунт и пароль из базы данных
                    await copy_account_and_password(message, id)
                    Counter.add_counter()
                except pyautogui.ImageNotFoundException:
                    pyautogui.click(938, 418, duration=0.25)
                    pyautogui.sleep(3)
                    # Активируем код
                    db = Database("tgbot/services/Database/codes.db")
                    db.execute(f"UPDATE CODES SET IsUse = TRUE WHERE code = '{code[0]}'")
                    break
            else:
                await message.answer("Коды закончились.")
    await message.answer(f'120 UC закинул на {id}')


async def copy_account_and_password(message: Message, id: str):
    await proxy_run()
    # Извлекаем следующий аккаунт и пароль из базы данных
    db = Database("tgbot/services/Database/codes.db")
    account_and_password = db.execute(
        f"SELECT login, pass FROM ACCOUNTS ORDER BY id ASC LIMIT 1 OFFSET {Counter.COUNTER}", fetchone=True)

    # Если аккаунт и пароль существуют, копируем их в буфер обмена
    if account_and_password:
        pyautogui.click(879, 26, duration=0.25)
        pyautogui.click(1133, 358, duration=0.25)
        pyautogui.click(1486, 157, duration=0.25)
        pyautogui.sleep(6)
        pyperclip.copy(account_and_password[0])
        acc = pyperclip.copy(account_and_password[0])
        pyautogui.click(975, 538, duration=0.25)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(960, 616, duration=0.25)
        pyperclip.copy(account_and_password[1])
        pyautogui.sleep(3)
        pyautogui.click(940, 620, duration=0.25)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(959, 745, duration=0.25)
        pyautogui.sleep(6)
        smena_id = pyautogui.locateOnScreen("tgbot/screenshots/Smena.png", confidence=0.9)
        pyautogui.click(smena_id, duration=0.25)
        pyautogui.click(952, 368, duration=0.25)
        pyautogui.click(1141, 371, duration=0.25)
        pyperclip.copy(id)
        pyautogui.click(936, 370, button='right', duration=0.25)
        pyautogui.sleep(1)
        pyautogui.click(991, 551, duration=0.25)
        pyautogui.click(968, 511, duration=0.25)
        pyautogui.sleep(1)
        await message.answer(f"Я сменил аккаунт на {acc}")
    else:
        await message.answer("К сожалению, в базе данных нет аккаунтов и паролей.")


def register_120(dp: Dispatcher):
    dp.register_message_handler(press_button_120, text='120')
    dp.register_message_handler(answer_id_120, state=InputId_120.Id)
