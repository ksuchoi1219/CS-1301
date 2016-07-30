# Kwang Su Choi & Rachael DePriest
# CS 1301 B5
# Kwang Su Choi (902969968) & Rachael DePriest (902906726)
# kchoi20@gatech.edu & rdepriest3@gatech.edu
# We worked on this homework assignment alone, using only this semester's course materials.


from Myro import *
init(S)

def filming():
    film = input("P = take a picture, S = stop")
    picList = []
    i = 0 
    while i in range(180):
        if film == "P":
            pic = takePicture()
            show(pic)
            picList.append(pic)
            savePicture(picList,"/Users/rnd0501/Documents/CS/robot.gif")
            film = input("P = take a picture, S = stop")
        elif film == "S":
            return
        else:
            print("please choose S or P")
            film = input("P = take a picture, S = stop")

def filming2(): #because the filming function was taking to long to update the aList when it got large, so we created another file 
    film = input("P = take a picture, S = stop")
    picList = []
    i = 0 
    while i in range(180):
        if film == "P":
            pic = takePicture()
            show(pic)
            picList.append(pic)
            savePicture(picList,"/Users/rnd0501/Documents/CS/robot2.gif")
            film = input("P = take a picture, S = stop")
        elif film == "S":
            return
        else:
            print("please choose S or P")
            film = input("P = take a picture, S = stop")