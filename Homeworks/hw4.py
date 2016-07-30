#Kwang Su Choi
#CS 1301 B5
#902969968
#kchoi20@gatech.edu
#I,Kwang Su Choi, have worked on this assignment alone using only course materials.

from Myro import*
init("COM40")

def danceOff():
    #the beginning
    turnBy(180)
    forward(2,1)
    backward(1,0.5)
    forward(3,0.7)
    turnRight(3,1)
    turnLeft(3,1.6)
    #popping
    turnRight(2,2.5)
    forward(3,1)
    backward(1,0.5)
    forward(3,0.2)
    backward(1.5,0.5)
    forward(3,0.3)
    backward(1.8,0.5)
    turnRight(2.5,0.8)
    backward(1,0.5)
    #sexy dance
    turnRight(2,1)
    turnLeft(2,1)
    turnBy(180)
    forward(2.4,0.9)
    turnBy(100)
    turnRight(2.5,1)
    turnLeft(2.5,1)
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

    aList = [1400,1400,1500,1700,1700,1500,1400,1250,1100,1100,1250,1400,1400,1250,1250,1250,1400,1400,1500,1700,1700,1500,1400,1250,1100,1100,1250,1400,1250,1250,1100,1100,1100]
    for note in aList:
         beep (0.4,note)


def remoteControl():
    menu = """Which dance step/song would you like?
            1. Forward for half a second
            2. Reverse direction (180 degrees)
            3. Turn right (90 degrees)
            4. Turn left (90 degrees)
            0. Exit"""
    userInput = int (input(menu))
    while True:
        if userInput == 1:
            forward(1,0.5)
        elif userInput == 2:
            turnBy(180)
        elif userInput == 3:
            turnBy(90)
        elif userInput == 4:
            turnBy(-90)
        elif userInput == 0:
            print("See you later!")
            return
        else:
            print("I'm sorry, that's not a valid choice")
        userInput = int (input(menu))





