
mainMonitor = 1 #Display count begins at 1, so 1 is the first display.

brightnessMethodChoice = 2 

"""

Brightness method 1 averages the brightness from all detected pixels.

Brightness method 2 averages the brightness from only the top 3 whitest pixels. 

"""

brightnessMin = 0 #The minimum percentage this program can change your brightness to

brightnessMax = 100 #The maximum percentage this program can change your brightness to

updateDelay = 1 #Times the program updates the brightness, in seconds






import mss as sct
import mss.tools
import time
import screen_brightness_control as sbc

orderedGrayValueList = []

targetedPixels = []

grayValueList = []

mainMonitorSBC = mainMonitor - 1

#SBC uses screen zero as first screen, but MSS uses screen one as first screen. MSS screen zero is all screens combined

targetDarknessValue = 50

def brightnessMethod(method):

    # gray value SHOULD be a value from zero to one

    if method == 1:
        targetDarknessValue = (sum(grayValueList)/len(grayValueList))*100
        return targetDarknessValue
    elif method == 2:
        
        topThird = max(1, len(orderedGrayValueList) // 3)
        combinedBrightness = 0

        for i in range(topThird):
            combinedBrightness = combinedBrightness + orderedGrayValueList[i]
            
        brightnessOutput = (combinedBrightness / topThird)*100
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
    
    monitor = sct.monitors[mainMonitor]
    monitorWidth = monitor["width"]
    monitorHeight = monitor["height"]


    while True:

        for targetX in range(3): #finds pixels and notes them in tuple
            for targetY in range(3):
                print(f"Finding height {targetY} at width {targetX}")

                print("TARGETING AT")
                print(round((1/3)*monitorWidth + ((1/9)*monitorWidth)*targetX))
                targetedPixels.append((
                    round((1/3)*monitorWidth + ((1/9)*monitorWidth)*targetX),
                    round((1/3)*monitorHeight + ((1/9)*monitorHeight)*targetY)
                    )
                )



        for i in range(9): #rolls through each coordinate in the tuple, finding their rgb values

            target = {"top":targetedPixels[i][1], "left":targetedPixels[i][0], "width":1, "height":1}

            print(targetedPixels)

            cap = sct.grab(target)

            r, g, b = cap.pixel(0,0)

            grayValue = 0.299 * (r/256) + 0.587 * (g/256) + 0.114 * (b/256)
            grayValueList.append(grayValue)



        orderedGrayValueList = sorted(grayValueList, reverse=True) #sorts all the numbers from highest to lowest


        print(orderedGrayValueList)


        targetDarknessValue = brightnessMethod(1)

        targetDarknessValue = (((brightnessMax - brightnessMin)/100)*targetDarknessValue)+brightnessMin


        targetDarknessValue = max(1, targetDarknessValue)
        targetDarknessValue = min(99, targetDarknessValue)

    
        sbc.set_brightness(targetDarknessValue, display=mainMonitorSBC)

        print(f"brightness percent aimed at {targetDarknessValue}")

        print("Clearing")
        targetedPixels.clear()
        grayValueList.clear()
        orderedGrayValueList.clear()

        time.sleep(updateDelay)
