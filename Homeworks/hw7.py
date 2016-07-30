# Kwang Su Choi & Miles Reardon
# CS 1301 B5
# Kwang Su Choi (902969968) & Miles Reardon (902976130)
# kchoi20@gatech.edu & miles.reardon@gmail.com
# We worked on this homework assignment alone, using http://cs.brynmawr.edu/~dkumar/Myro/Text/Fall08/PDF/MyroOverview.pdf for materials on pictures.


from Myro import*
init()

def seeingRed():
    apic = takePicture()
    show(apic)
    for x in range(getWidth(apic)):
        for y in range(getHeight(apic)):
            pixel=getPixel(apic,x,y)
            setBlue(pixel,(getBlue(pixel)*0.3))
            setGreen(pixel,(getGreen(pixel)*0.3))
    savePicture(apic,"seeingRed.jpg")


#for fade, make sure you open it with Internet Explorer! We don't know it would work for other browser or program, but it works for Internet Explorer.
def fade():
    apic = takePicture()
    show(apic)
    aList=[apic]
    for iteration in range(20):
        for x in range(getWidth(apic)):
            for y in range(getHeight(apic)):
                pixel=getPixel(apic,x,y)
                setRed(pixel,int(getRed(pixel)*0.7))
                setGreen(pixel,int(getGreen(pixel)*0.7))
                setBlue(pixel,int(getBlue(pixel)*0.7))
        aList.append(copyPicture(apic))


    savePicture(aList,"fade.gif")
    return aList


def overlay():
    apic = takePicture()
    show(apic)
    for x in range(10,20):
        for y in range(20,50):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    for x in range(20,30):
        for y in range(20,30):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    for x in range(30,40):
        for y in range(20,50):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    for x in range(50,60):
        for y in range(20,50):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    for x in range(60,70):
        for y in range(20,30):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    for x in range(60,70):
        for y in range(40,50):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    for x in range(70,80):
        for y in range(20,50):
            pixel=getPixel(apic,x,y)
            setRed(pixel,255)
            setBlue(pixel,255)
            setGreen(pixel,255)
    show(apic)
    savePicture(apic,"overlay.jpg")

def multipleExposure():
    pic1 = makePicture(loadPicture(pickAFile()))
    pic2 = makePicture(loadPicture(pickAFile()))
    show(pic1)

    redlist1 = []
    greenlist1 = []
    bluelist1 = []

    redlist2 = []
    greenlist2 = []
    bluelist2 = []

    finalrlist = []
    finalglist = []
    finalblist = []

    for pixel in getPixels(pic1):
        red1 = [getRed(pixel)]
        green1 = [getGreen(pixel)]
        blue1 = [getBlue(pixel)]
        redlist1 = redlist1 + red1
        greenlist1 = greenlist1 + green1
        bluelist1 = bluelist1 + blue1

    for pixel in getPixels(pic2):
        red2 = [getRed(pixel)]
        green2 = [getGreen(pixel)]
        blue2 = [getBlue(pixel)]
        redlist2 = redlist2 + red2
        bluelist2 = bluelist2 + blue2
        greenlist2 = greenlist2 + green2

    pixNum = getHeight(pic1)*getWidth(pic1)
    for x in range(0,pixNum):
        finalrlist = finalrlist + [(redlist1[x]+redlist2[x])/2]
        finalglist = finalglist + [(greenlist1[x]+greenlist2[x])/2]
        finalblist = finalblist + [(bluelist1[x]+bluelist2[x])/2]
    x=0
    for pixel in getPixels(pic1):
        setRed(pixel,finalrlist[x])
        setGreen(pixel,finalglist[x])
        setBlue(pixel,finalblist[x])
        x = x+1
    show(pic1)
    savePicture(pic1, "me_after.jpg")


def GreenScreen():
    background = makePicture(loadPicture(pickAFile()))
    greenScreen = makePicture("greenscreen.jpg")
    show(greenScreen)

    redlistbg = []
    bluelistbg = []
    greenlistbg = []

    redlistgs = []
    bluelistgs = []
    greenlistgs = []
    x = 0

    for pixel in getPixels(background):
        r = [getRed(pixel)]
        g = [getGreen(pixel)]
        b = [getBlue(pixel)]
        redlistbg = redlistbg + r
        bluelistbg = bluelistbg + b
        greenlistbg = greenlistbg + g

    for pixel in getPixels(greenScreen):
        r1 = getRed(pixel)
        g1 = getGreen(pixel)
        b1 = getBlue(pixel)
        if g1 >=250 and b1 <= 5 and r1 <= 5:
            setRed(pixel, redlistbg[x])
            setGreen(pixel, greenlistbg[x])
            setBlue(pixel, bluelistbg[x])
        x = x+1


    savePicture(greenScreen,"greenscreen_after.jpg")