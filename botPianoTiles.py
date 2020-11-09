from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pyautogui.displayMousePosition()


y = 674
x1 = 750
x2 = 900
x3 = 1030
x4 = 1200


def clickT(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while keyboard.is_pressed('q') == False:

    if pyautogui.pixelMatchesColor(x1, y, (17,17,17)):
        clickT(x1, y)

    if pyautogui.pixelMatchesColor(x2, y, (17,17,17)):
        clickT(x2, y)

    if pyautogui.pixelMatchesColor(x3, y, (17,17,17)):
        clickT(x3, y)

    if pyautogui.pixelMatchesColor(x4, y, (17,17,17)):
        clickT(x4, y)