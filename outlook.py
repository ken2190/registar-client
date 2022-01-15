import pyautogui

import autogui
from autogui import switch_to_eng
import config
import registar
from generator import generate_user


def register():
    autogui.open_browser(config.OUTLOOK_REG)
    autogui.wait_img("resources/outlook-ready.png")
    pyautogui.press('tab', presses=3, interval=0.1)
    pyautogui.press('enter')
    generated = generate_user("outlook.com")
    switch_to_eng()
    pyautogui.write(generated.email, interval=0.05)
    pyautogui.press('tab', presses=4, interval=0.1)
    pyautogui.press('enter')
    autogui.wait_img("resources/outlook-ready-2.png")
    pyautogui.press('tab')
    pyautogui.write(generated.password, interval=0.05)
    pyautogui.press('tab', presses=5, interval=0.1)
    pyautogui.press('enter')
    autogui.wait_img("resources/outlook-ready-3.png")
    pyautogui.press('tab', presses=2, interval=0.1)
    pyautogui.write(generated.lastname, interval=0.05)
    pyautogui.press('tab')
    pyautogui.write(generated.firstname, interval=0.05)
    pyautogui.press('enter')
    autogui.wait_img("resources/outlook-ready-4.png")
    pyautogui.press('tab', presses=2, interval=0.1)
    pyautogui.write(str(generated.birthDate.day), interval=0.05)
    pyautogui.press('tab')
    pyautogui.press('down', presses=generated.birthDate.month, interval=0.1)
    pyautogui.press('tab')
    pyautogui.write(str(generated.birthDate.year), interval=0.05)
    pyautogui.press('enter')
    autogui.wait_img("resources/outlook-ready-5.png")

    registar.user_add(generated)


register()
