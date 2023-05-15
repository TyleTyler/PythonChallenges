import pyautogui
import os


currentDic = os.path.join(os.getcwd(), "pyLocate", "buttons")
print(currentDic)

def clickBut(symbol):
    x, y= pyautogui.locateCenterOnScreen(f'{currentDic}\\{symbol}.png', confidence = 0.9)
    pyautogui.moveTo(x, y, duration = 0.1)
    pyautogui.leftClick()
    
while True:
    userIn = input("Insert a symbol ")
    # clickBut(userIn)
    for x in userIn:
        clickBut(x)

