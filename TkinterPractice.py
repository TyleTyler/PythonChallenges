
from tkinter import *
from pythonScreenshot import takeScreenShot
import keyboard

def sayHello():
    print("Hello")

#window
window = Tk()
window.geometry("1920x1080")

#labels
titleLable = Label(window, text="I will say hello")
button = Button(master=window, text="Greet", command=sayHello   )
button.pack()
titleLable.pack(pady=10)


window.mainloop()

# while True:
#     try:
#         if keyboard.is_pressed("p"):
#             takeScreenShot()
#         elif keyboard.is_pressed("ctrl + m"):
#             break
#         else:
#             pass
#     except:
#         print("Could not take a screen shot")
#         break