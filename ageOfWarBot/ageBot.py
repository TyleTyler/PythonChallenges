import pyautogui
import os
import time
from timer import timer
from PIL import Image
import cv2 as cv
import numpy as npk

currentDic = os.path.join(os.getcwd(), "ageOfWarBot", "graphics")


# time.sleep(2)
# x, y= pyautogui.locateCenterOnScreen(f'{currentDic}\moneySymbol.png', confidence = 0.9)
# screenShot = pyautogui.screenshot(region=(x + 15 , y - 7, 40, 29 ))
# screenShotAr = np.array(screenShot)


img = cv.imread(cv.samples.findFile("ageOfWarBot\graphics\money.png"), 2)
cv.imshow("Display window", img)
cv.imwrite(f'{currentDic}\\test.png', img)