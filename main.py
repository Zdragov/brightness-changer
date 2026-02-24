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



    targetedPixels.append((round((1/3)*monitorWidth), round((1/3)*monitorHeight)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*1), round((1/3)*monitorHeight)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*2), round((1/3)*monitorHeight)))


    targetedPixels.append((round((1/3)*monitorWidth), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*1)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*1), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*1)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*2), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*1)))


    targetedPixels.append((round((1/3)*monitorWidth), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*2)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*1), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*2)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*2), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*2)))

    print(targetedPixels)



"""

for i in range(3):
    
    for j in range(3):
        print(f"height {j} at width {i}")
    

"""



