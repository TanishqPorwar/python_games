import pyautogui
from pynput.keyboard import Key, Controller
import time

s = "python3 share_review.py --image ~/booyah-inc.jpg --message 'this is Tanishq’s favorite ice-cream!'"
s = s.split()

# pyautogui.hotkey("alt", "tab")
time.sleep(2)
for i in s:
    pyautogui.typewrite(i)
    pyautogui.press('space')
