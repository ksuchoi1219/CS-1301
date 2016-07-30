#Rachael DePriest &John Mattle and Kwang Su Choi
#Rachael DePriest(902906726) and Kwang Su Choi (902969968)
#kchoi20@gatech.edu
#we completed this assignment using only this semester's course materials 


#green screen for editing in flowershop
#sets top half of picture to black
#anything that is extremely dark will be changed to flowshop background

from Myro import *

def blackScreen(aPic,backGround):
    height=getHeight(aPic)
    for pixel in getPixels(aPic):
        y=getY(pixel)
        if y<(height/1.3):
            setRGB(pixel,(0,0,0))
        if (getGreen(pixel)) < 20 and (getRed(pixel))< 20 and getBlue(pixel)< 20:
                x = getX(pixel)
                y = getY(pixel)
                pix = getPixel(backGround,x,y)
                setRed(pixel,getRed(pix))
                setBlue(pixel,getBlue(pix))
                setGreen(pixel,getGreen(pix))
    show(aPic)
    savePicture(aPic,"/Users/rnd0501/Desktop/flowershop.jpg")


#splitscreen issues
#splitscreen would require cutting the top halves or bottom halves of two pictures and putting them into one
#this would not work with our pictures since it would cut each robot in half

#grayscale effect
#any pic
#might be good at beginning
def greyScale(pic):
    for pixel in getPixels(pic):
        average = (getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3
        setRed(pixel, average)
        setGreen(pixel, average)
        setBlue(pixel, average)

#takes in pic
#shows 3 pics with shutter idea
#for robotpic2
def blinkBlack(pic):
    copy1=copyPicture(pic)
    copy2=copyPicture(pic)
    copy3=copyPicture(pic)
    height=getHeight(pic)
    for pixel in getPixels(copy1):
        Y=getY(pixel)
        if Y<(height/4) or Y>(3*height/4):
            setRGB(pixel,(0,0,0))
    for pixel in getPixels(copy2):
        Y=getY(pixel)
        if Y<(height/3) or Y>(2*height/3):
            setRGB(pixel,(0,0,0))
    for pixel in getPixels(copy3):
        setRGB(pixel,(0,0,0))
    show(copy1)
    show(copy2)
    show(copy3)
    savePicture(copy1,"/Users/rnd0501/Desktop/copy1.jpg")
    savePicture(copy2,"/Users/rnd0501/Desktop/copy2.jpg")
    savePicture(copy3,"/Users/rnd0501/Desktop/copy3.jpg")

#function used for both fade black and fade slides
def editPic(pic):
    pic1 = copyPicture(pic)
    for pix in getPixels(pic1):
        (r,g,b) = getRGB(pix)
        setColor(pix, makeColor(2 * r // 3, 2 * g // 3, b // 2))
    return pic1

#for fading from pic3 to pic4
#it fades close to black then fades back up as pic4
def fadeSlides():

    pic = makePicture("/Users/rnd0501/Desktop/robotpic3.jpg")
    pic2 = makePicture("/Users/rnd0501/Desktop/robotpic4.jpg")
    picList = [pic]
    for num in range(10):
        edit = editPic(pic)
        picList.append(edit)
        pic = edit
    for num in range(1,11):
        temp = pic2
        for pix in getPixels(temp):
            (r,g,b) = getRGB(pix)
            setColor(pix, makeColor(r//10*num, g//10*num, b//10*num))
        picList.append(temp)
    savePicture(picList,"/Users/rnd0501/Documents/CS HW 8/fade.gif")

#for pic4
#fades to black for end 
def fadeToBlack():

    pic = makePicture("/Users/rnd0501/Desktop/robotpic4.jpg")
    picList = [pic]
    for num in range(20):
        edit = editPic(pic)
        picList.append(edit)
        pic = edit
    for pix in getPixels(pic):
        setColor(pix, makeColor(0,0,0))
    picList.append(pic)
    savePicture(picList,"/Users/rnd0501/Documents/CS HW 8/fadetoblack.gif")



