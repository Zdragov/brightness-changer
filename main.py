import mss as sct
import mss.tools


import pyautogui

import time



import screen_brightness_control as sbc


orderedGrayValueList = []

targetedPixels = []

grayValueList = []

mainMonitor = 0


mousex, mousey = pyautogui.position()

def brightnessMethod(method):
    if method == 1:
        totalDarknessValue = (sum(grayValueList)/len(grayValueList))




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


    while True:

        for targetX in range(3):
            
            for targetY in range(3):
                print(f"Finding height {targetY} at width {targetX}")
                targetedPixels.append((
                    round((1/3)*monitorWidth + ((1/9)*monitorWidth)*targetX),
                    round((1/3)*monitorHeight + ((1/9)*monitorHeight)*targetY)
                    )
                )

        for i in range(9):

            target = {"top":targetedPixels[i][1], "left":targetedPixels[i][0], "width":1, "height":1}

            cap = sct.grab(target)

            r, g, b = cap.pixel(0,0)

            grayValue = 0.299 * r + 0.587 * g + 0.114 * b

            grayValueList.append(round(grayValue))

            print(r, g, b)

            print(i)

        print(targetedPixels)

        print(grayValueList)

    

        totalDarknessValue = (sum(grayValueList)/len(grayValueList))

        print(orderedGrayValueList)

        

        





        orderedGrayValueList = sorted(grayValueList, reverse=True)
        
        top3count = max(1, len(orderedGrayValueList) // 3)

        x = 0

        for i in range(top3count):
            
            x = x + orderedGrayValueList[i]
            
        y = (x / top3count)/2

        print(f"y is{y}")










        sbc.set_brightness(50, display=mainMonitor)



        print(f"brightness percent aimed at {totalDarknessValue}")

        print("Clearing")
        targetedPixels.clear()
        grayValueList.clear()

        time.sleep(999)


























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







    targetedPixels.append((round((1/3)*monitorWidth), round((1/3)*monitorHeight)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*1), round((1/3)*monitorHeight)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*2), round((1/3)*monitorHeight)))


    targetedPixels.append((round((1/3)*monitorWidth), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*1)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*1), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*1)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*2), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*1)))


    targetedPixels.append((round((1/3)*monitorWidth), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*2)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*1), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*2)))

    targetedPixels.append((round((1/3)*monitorWidth + ((1/9)*monitorWidth)*2), round((1/3)*monitorHeight + ((1/9)*monitorHeight)*2)))

    



    
    """