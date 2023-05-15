import win32clipboard
import os
import keyboard

while True:
    if keyboard.is_pressed("ctrl + b"):
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        os.system(f'start https://google.com//search?q={data}')
        win32clipboard.CloseClipboard()

