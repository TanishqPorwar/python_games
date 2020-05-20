import pyautogui
from PIL import Image, ImageGrab
# import numpy as np
import time


def hit(key):
    pyautogui.keyDown(key)


def release(key):
    pyautogui.keyUp(key)


def changeWindow():
    """ changes window to the last open window
        here it is the chrome dino game """
    hit("alt")
    hit("tab")
    release("tab")
    release("alt")


def takeScreenshot():
    # Imagegrab.grab() takes a screenshot
    # convert("L") converts the screenshot to gray scale
    image = ImageGrab.grab().convert("L")
    return image


def isCollide():
    # for i in range(720, 800):
    #     for j in range(470, 500):
    #         if data[i, j] < 80:
    #             hit("down")
    #             release("down")
    #             return True
    for i in range(720, 800):
        for j in range(500, 530):
            if data[i, j] < 100:
                hit("space")
                release("space")
                return True
    return False


if __name__ == "__main__":
    changeWindow()
    # wait for the screen to change
    time.sleep(1)
    # hit("space")
    # release("space")
    # while True:
    #     image = takeScreenshot()
    #     data = image.load()
    #     isCollide()

    image = takeScreenshot()
    data = image.load()
    # scan for cactus
    for i in range(720, 780):
        for j in range(510, 530):
            data[i, j] = 80
    # scan for bird
    for i in range(720, 780):
        for j in range(470, 492):
            data[i, j] = 00
    image.show()
