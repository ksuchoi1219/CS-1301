# Kwang Su Choi & Miles Reardon
# CS 1301 B5
# Kwang Su Choi (902969968) & Miles Reardon (902976130)
# kchoi20@gatech.edu & miles.reardon@gmail.com
# We worked on this homework assignment alone, using only this semester's course materials.

from Myro import*
init()

from random import randint

randomTime=(randint(1,10))

def defineColors():
    redCounter = 0
    greenCounter = 0
    blueCounter = 0
    yellowCounter = 0
    totalCounter = 0
    turnRight(1,randomTime)
    pic = takePicture()
    show(pic)
    #in window, get pixels and define colors. If it can't find color, turn again.
    for x in range((getWidth(pic)//3),(getWidth(pic)//3)*2):
        for y in range(getHeight(pic)//3,(getHeight(pic)//3*2)):

            pixel = getPixel(pic,x,y)
            r,g,b = getRGB(pixel)

            if r>g+10 and r>b+10:
                redCounter = redCounter + 1
            elif b>r+10 and b>g+10:
                blueCounter = blueCounter + 1
            elif g>r+10 and g>b+10:
                greenCounter = greenCounter + 1
            elif r>g+10 and g>r+10 and r>b+10 and g>b+10:
                yellowCounter = yellowCounter + 1

    if redCounter>blueCounter and redCounter>greenCounter and redCounter>yellowCounter:
        aList = [1400,1400,1500,1700,1700,1500,1400,1250,1100,1100,1250,1400,1400,1250,1250,1250,1400,1400,1500,1700,1700,1500,1400,1250,1100,1100,1250,1400,1250,1250,1100,1100,1100]
        for note in aList:
            beep (0.4,note)
    elif blueCounter>redCounter and blueCounter>greenCounter and blueCounter>yellowCounter:
        l,c,r = getObstacle()
        while (l < 100 and c < 100 and r < 100):
            print(l,c,r)
            l,c,r = getObstacle()
            forward(.5,1)
            stop()
    elif greenCounter>redCounter and greenCounter>blueCounter and greenCounter>yellowCounter:
        turnBy(180)
        forward(2,1)
        backward(1,0.5)
        forward(3,0.7)
        turnRight(3,1)
        turnLeft(3,1.6)
        turnBy(90)
        #time to shine
        forward(2,0.6)
        turnRight(2,1)
        forward(2,0.6)
        turnLeft(2,1)
        backward(2,1)
        forward(2,0.6)
        turnRight(3,1)
        turnLeft(3,0.5)
        turnBy(90)
    elif yellowCounter>redCounter and yellowCounter>greenCounter and yellowCounter>blueCounter:
        l,r = getIR()
        while (l != 0 and r != 0):
            l,r = getIR()
            backward(.5,1)
            print(l,r)
            stop()
    else:
        defineColors()


