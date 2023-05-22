import pyautogui
import os
import time
from PIL import Image
import cv2 as cv
import numpy as np
import keyboard

currentDic = os.path.join(os.getcwd(), "ageOfWarBot", "graphics")

while True:
    if keyboard.is_pressed("p"):
        x, y = pyautogui.locateCenterOnScreen(f'{currentDic}\moneySymbol.png', confidence=0.9)
        screenShot = pyautogui.screenshot(region=(x + 15, y - 7, 40, 29))

        ROI = np.array(screenShot, dtype='uint8')
        hsvShot = cv.cvtColor(ROI, cv.COLOR_RGB2HSV)

        # Define lower and upper bounds for yellow color in HSV
        lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
        upper_yellow = np.array([40, 255, 255], dtype=np.uint8)

        # Create a mask based on the yellow color range
        mask = cv.inRange(hsvShot, lower_yellow, upper_yellow)

        # Apply the mask to the original image
        extracted_numbers = cv.bitwise_and(ROI, ROI, mask=mask)

        # Convert the result to grayscale
        gray = cv.cvtColor(extracted_numbers, cv.COLOR_BGR2GRAY)

        # Apply thresholding for better contour detection
        ret,thresh = cv.threshold(gray,127,255,0)

        # Find contours in the thresholded image
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        for i, cnt in enumerate(contours):
            # Get bounding box coordinates for each contour
            x, y, w, h = cv.boundingRect(cnt)
            
            # Extract each number and save it as a separate image
            cv.imwrite(f"{currentDic}\\number_{i}.png", gray[y:y+h, x:x+w])

        cv.imwrite(f"{currentDic}\\test2.png", ROI)

        cv.imshow('Mask', mask)
        cv.imshow('Extracted Numbers', extracted_numbers)
        cv.imshow("Display window", cv.cvtColor(extracted_numbers, cv.COLOR_RGB2BGR))
        cv.waitKey(0)
        cv.destroyAllWindows()

    if keyboard.is_pressed("alt + p"):
        break