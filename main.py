import mss as sct
import mss.tools

import wmi

import pyautogui

import time



import screen_brightness_control as sbc


targetedPixels = []

mainMonitor = 1

print(sbc.get_brightness())

time.sleep(1)

print(pyautogui.position())

mousex, mousey = pyautogui.position()

print()


with mss.mss() as sct:

    monitor = sct.monitors[mainMonitor]
    monitorWidth = monitor["width"]
    monitorHeight = monitor["height"]

    print(f"Selector monitor dimensions: {monitorWidth}x{monitorHeight}")
    
    capture = {"top":mousey, "left":mousex, "width":1, "height":1}

    x = sct.grab(capture)

    r, g, b = x.pixel(0,0)

    print(r, g, b)
    
    grayValue = 0.299 * r + 0.587 * g + 0.114 * b

    print(grayValue)

    targetBrightness = grayValue / 2.56

    print(targetBrightness)

    sbc.set_brightness(50, display=mainMonitor)
    
    monitor = sct.monitors[mainMonitor]
    monitorWidth = monitor["width"]
    monitorHeight = monitor["height"]

    """
    
    targeted:

    1/3 to 2/3 of X
    1/3 to 2/3 of Y

    X

    (1/3)*monitorWidth

    (1/3)*monitorWidth + ((1/9)*monitorWidth)*1
    
    (1/3)*monitorWidth + ((1/9)*monitorWidth)*2



    (1/3)*monitorHeight

    (1/3)*monitorHeight + ((1/9)*monitorHeight)*1
    
    (1/3)*monitorHeight + ((1/9)*monitorHeight)*2
    
    """



    pos11 = (1/3)*monitorWidth, (1/3)*monitorHeight

    pos21 = (1/3)*monitorWidth + ((1/9)*monitorWidth)*1, (1/3)*monitorHeight

    pos31 = (1/3)*monitorWidth + ((1/9)*monitorWidth)*2, (1/3)*monitorHeight


    pos12 = (1/3)*monitorWidth, (1/3)*monitorHeight + ((1/9)*monitorHeight)*1

    pos22 = (1/3)*monitorWidth + ((1/9)*monitorWidth)*1, (1/3)*monitorHeight + ((1/9)*monitorHeight)*1

    pos32 = (1/3)*monitorWidth + ((1/9)*monitorWidth)*2, (1/3)*monitorHeight + ((1/9)*monitorHeight)*1


    pos13 = (1/3)*monitorWidth, (1/3)*monitorHeight + ((1/9)*monitorHeight)*2

    pos23 = (1/3)*monitorWidth + ((1/9)*monitorWidth)*1, (1/3)*monitorHeight + ((1/9)*monitorHeight)*2

    pos33 = (1/3)*monitorWidth + ((1/9)*monitorWidth)*2, (1/3)*monitorHeight + ((1/9)*monitorHeight)*2



"""

for i in range(3):
    
    for j in range(3):
        print(f"height {j} at width {i}")
    

"""



