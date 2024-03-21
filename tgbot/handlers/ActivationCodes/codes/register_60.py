import sqlite3

import pyautogui
import pyperclip
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc import InputId_60
from tgbot.services.Counter.counter import Counter
from tgbot.services.Database.sqlite import Database
from tgbot.services.chromiumdriver import proxy_run


async def press_button_60(message: Message):
    photo = "tgbot/screenshots/Smena.png"
    try:
        photo_id = pyautogui.locateOnScreen(photo, confidence=0.8)
        pyautogui.click(photo_id, duration=0.25)
        pyautogui.sleep(2)
        await message.answer("Введите ID")
        await InputId_60.Id.set()
    except:
        await message.answer("Не нашел изображение")


async def answer_id_60(message: Message, state: FSMContext):
    id = message.text
    await message.answer(f"Круто, ты ввел {id}")
    await state.finish()
    pyperclip.copy(id)
    pyautogui.click(935, 402, duration=0.25)
    pyautogui.click(1139, 403, duration=0.25)
    pyautogui.click(940, 401, button='right', duration=0.25)
    pyautogui.sleep(1)
    pyautogui.click(982, 596, duration=0.25)
    pyautogui.click(958, 471, duration=0.25)
    pyautogui.sleep(2)

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
            pyautogui.sleep(1)
            pyautogui.click(861, 755, duration=0.25)
            pyautogui.click(1070, 755, duration=0.25)
            pyautogui.click(889, 755, button='right', duration=0.25)
            pyautogui.sleep(1)
            pyautogui.click(931, 528, duration=0.25)
            pyautogui.click(1197, 755, duration=0.25)
            pyautogui.sleep(3)
            # Нажатие на Submit перед капчей
            pyautogui.click(944, 831, duration=0.25)
            pyautogui.sleep(3)
            # Проверяем, есть ли на экране кнопка "Я не робот"
            try:
                pyautogui.locateOnScreen('tgbot/screenshots/Captcha.png', confidence=0.9)
                # Копируем аккаунт и пароль из базы данных
                await copy_account_and_password(message, id)
                Counter.add_counter()
            except pyautogui.ImageNotFoundException:
                pyautogui.click(937, 474, duration=0.25)
                pyautogui.sleep(3)
                # Активируем код
                await message.answer(f'60 UC закинул на {id}')
                db = Database("tgbot/services/Database/codes.db")
                db.execute(f"UPDATE CODES SET IsUse = TRUE WHERE code = '{code[0]}'")
                break
        else:
            await message.answer("Коды закончились.")


async def copy_account_and_password(message: Message, id: str):
    await proxy_run()
    # Извлекаем следующий аккаунт и пароль из базы данных
    db = Database("tgbot/services/Database/codes.db")
    account_and_password = db.execute(
        f"SELECT login, pass FROM ACCOUNTS ORDER BY id ASC LIMIT 1 OFFSET {Counter.COUNTER}", fetchone=True)

    # Если аккаунт и пароль существуют, копируем их в буфер обмена
    if account_and_password:
        pyautogui.click(874, 30, duration=0.25)
        pyautogui.click(1131, 366, duration=0.25)
        pyautogui.click(1482, 172, duration=0.25)
        pyautogui.sleep(6)
        pyperclip.copy(account_and_password[0])
        acc = account_and_password[0]
        pyautogui.click(915, 546, duration=0.25)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(959, 629, duration=0.25)
        pyperclip.copy(account_and_password[1])
        pyautogui.sleep(3)
        pyautogui.click(944, 632, duration=0.25)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(956, 758, duration=0.25)
        pyautogui.sleep(6)
        smena_id = pyautogui.locateOnScreen("tgbot/screenshots/Smena.png", confidence=0.9)
        pyautogui.click(smena_id, duration=0.25)
        pyautogui.click(935, 402, duration=0.25)
        pyautogui.click(1139, 403, duration=0.25)
        pyperclip.copy(id)
        pyautogui.click(940, 401, button='right', duration=0.25)
        pyautogui.sleep(1)
        pyautogui.click(982, 596, duration=0.25)
        pyautogui.click(958, 471, duration=0.25)
        pyautogui.sleep(2)
        await message.answer(f"Я сменил аккаунт на {acc}")
    else:
        await message.answer("К сожалению, в базе данных нет аккаунтов и паролей.")


def register_60(dp: Dispatcher):
    dp.register_message_handler(press_button_60, text='60')
    dp.register_message_handler(answer_id_60, state=InputId_60.Id)
