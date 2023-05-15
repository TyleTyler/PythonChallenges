import os
import pyautogui
import cv2
from PIL import Image
import numpy as np
import keyboard

def takeScreenShot():
    currentDic = os.path.join(os.getcwd(), "screenShots")
    listDir = os.listdir(currentDic)
    screenShot = pyautogui.screenshot()
    imageData = np.asarray(screenShot)
    for count, file in enumerate(listDir):
        try: 
            first = int(file.split(".")[0][-1])
            after = int(listDir[count + 1].split(".")[0][-1])
            if(after != first + 1):
                print("There is a missing index" + after + " is missing")
                result = cv2.imwrite(f"{currentDic}\screen{after}.png", cv2.cvtColor(imageData, cv2.COLOR_RGB2BGR))
        except:
            nextIndex = int(file.split(".")[0][-1])
            result = cv2.imwrite(f"{currentDic}\screen{nextIndex + 1}.png", cv2.cvtColor(imageData, cv2.COLOR_RGB2BGR))
            break

# while True:
#     try:
#         if keyboard.is_pressed("p"):
#             takeScreenShot()
#         elif keyboard.is_pressed("ctrl + p"):
#             break
#         else:
#             pass
#     except:
#         print("Could not take a screen shot")
#         break
