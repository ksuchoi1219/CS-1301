#Kwang Su Choi
#CS 1301 B5
#902969968
#kchoi20@gatech.edu
#I,Kwang Su Choi, have worked on this assignment alone using only course materials.


def machToFPS():
    response = input("Enter the speed in mach")
    x = float(response)
    mach = x*1116.4370079
    print(response,"mach is",mach,"feet/second.")


def sqPyramidVolume():
    length = input("What is the length of your base in inches?")
    l=float(length)
    height = input("What is the height of your base in inches?")
    h=float(height)
    volume=(l*l*h)/3
    print("Volume of your square pyramid is",volume,"inches-cubed.")


def makeChange():
    response = input("How many cents do you have?")
    x=int(response)
    dollar = int(x/100)
    quarter = int((x%100)/25)
    dime = int((x%100%25)/10)
    nickel = int((x%100%25%10)/5)
    pennies = int((x%100%25%10%5)/1)
    print ("You have",dollar,"dollars,",quarter,"quarter,",dime,"dime,",nickel,"nickel,",pennies,"pennies.")


def PPIIndex ():
    weight = input("How much do you weight in pounds?")
    w=float (weight)
    height = input("How tall are you in inches?")
    h=float (height)
    result = w/h*1.125
    print("Your corrected PPI is {:.1f}.".format(result))


