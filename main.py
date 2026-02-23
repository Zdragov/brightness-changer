import mss as sct
import mss.tools

import wmi

import pyautogui

import time

import screen_brightness_control as sbc

mainmonitor = 0

print(sbc.get_brightness())

time.sleep(1)

print(pyautogui.position())

mousex, mousey = pyautogui.position()

print()


with mss.mss() as sct:

    capture = {"top":mousey, "left":mousex, "width":1, "height":1}

    x = sct.grab(capture)

    r, g, b = x.pixel(0,0)

    print(r, g, b)
    
    gray = 0.299 * r + 0.587 * g + 0.114 * b

    print(gray)

    sbc.set_brightness(50, display=mainmonitor)
    
    
    



