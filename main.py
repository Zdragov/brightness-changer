brightnessMethodChoice = 2

import mss as sct
import mss.tools


import pyautogui

import time



import screen_brightness_control as sbc


orderedGrayValueList = []

targetedPixels = []

grayValueList = []

mainMonitor = 0

targetDarknessValue = 50

def brightnessMethod(method):
    if method == 1:
        targetDarknessValue = (sum(grayValueList)/len(grayValueList))
        return targetDarknessValue
    elif method == 2:
        
        
        topThird = max(1, len(orderedGrayValueList) // 3)

        combinedBrightness = 0

        for i in range(topThird):
            
            combinedBrightness = combinedBrightness + orderedGrayValueList[i]
            
        brightnessOutput = (combinedBrightness / topThird)/2.56

        print(f"y is{brightnessOutput}")

        return brightnessOutput
    

    else:
        targetDarknessValue = (sum(grayValueList)/len(grayValueList))
        return targetDarknessValue




with mss.mss() as sct:

    monitor = sct.monitors[mainMonitor]
    monitorWidth = monitor["width"]
    monitorHeight = monitor["height"]

    print(f"Selector monitor dimensions: {monitorWidth}x{monitorHeight}")
    
    #capture = {"top":mousey, "left":mousex, "width":1, "height":1}

    #x = sct.grab(capture)

    #r, g, b = x.pixel(0,0)

    #print(r, g, b)
    
    #grayValue = 0.299 * r + 0.587 * g + 0.114 * b

    #print(grayValue)

    #targetBrightness = grayValue / 2.56

    #print(targetBrightness)

    #sbc.set_brightness(50, display=mainMonitor)
    
    monitor = sct.monitors[mainMonitor]
    monitorWidth = monitor["width"]
    monitorHeight = monitor["height"]


    while True:

        for targetX in range(3): #finds pixels and notes them in tuple
            for targetY in range(3):
                print(f"Finding height {targetY} at width {targetX}")
                targetedPixels.append((
                    round((1/3)*monitorWidth + ((1/9)*monitorWidth)*targetX),
                    round((1/3)*monitorHeight + ((1/9)*monitorHeight)*targetY)
                    )
                )



        for i in range(9): #rolls through each coordinate in the tuple, finding their rgb values

            target = {"top":targetedPixels[i][1], "left":targetedPixels[i][0], "width":1, "height":1}

            cap = sct.grab(target)

            r, g, b = cap.pixel(0,0)

            grayValue = 0.299 * (r/256) + 0.587 * (g/256) + 0.114 * (b/256)
            grayValueList.append(round(grayValue))



        orderedGrayValueList = sorted(grayValueList, reverse=True) #sorts all the numbers from highest to lowest


        print(orderedGrayValueList)





        targetDarknessValue = brightnessMethod(1)


        targetDarknessValue = max(1, targetDarknessValue)
        targetDarknessValue = min(99, targetDarknessValue)


        

    
        sbc.set_brightness(targetDarknessValue, display=mainMonitor)

        print(f"brightness percent aimed at {targetDarknessValue}")

        print("Clearing")
        targetedPixels.clear()
        grayValueList.clear()
        orderedGrayValueList.clear()

        time.sleep(1)


























