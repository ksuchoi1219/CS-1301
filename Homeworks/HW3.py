#Kwang Su Choi
#CS 1301 B5
#902969968
#kchoi20@gatech.edu
#I,Kwang Su Choi, have worked on this assignment alone using only course materials.




def letterGrade(grade):
    if int(grade)<=100 and int(grade) >=90:
        return ("You made a(n) A.")
    elif int(grade)<=90 and int(grade) >=80:
        return ("You made a(n) B.")
    elif int(grade) <=80 and int(grade) >=70:
        return("You made a(n) C.")
    elif int(grade) <=70 and int(grade) >=60:
        return("You made a(n) D.")
    else:
        return("You made a(n) F.")


def countLetter(aWord,aLetter):
    count = 0
    for x in aWord:
        if aLetter == x:
            count = count + 1
    return(count)


def eyeForI(aString):
    aNewString = ""
    for x in aString:
        if x == "i" or x == "I":
            newWord = "eye"
            aNewString = aNewString + newWord
        else:
            aNewString = aNewString + x
    return (aNewString)


def wordMirror(aString):
    aNewString = ""
    for i in aString:
        aNewString = i + aNewString
    aNewString = aString + aNewString
    return (aNewString)
    


def encryption(aString):
    for i in aString:
        aNewString = aString.replace("a","@").replace("e","()").replace("h","#").replace("l","1").replace("r","+").replace("s","$").replace("v","^").replace("x","*")
    print ("The encrypted code is:",aNewString)



def guessPassword(rightPassword):
    userPassword = input("Please enter the password")
    rightPassword = "abcd1234"
    while userPassword !="abcd1234":
        print("Incorrect password!")
        userPassword = input("Please enter the password")
    print("You entered the correct password!")


def countDown(startNum,countBy):
    while startNum > 0:
        print (startNum)
        startNum = startNum - countBy
    print ("Blast Off!")


def numberBowTie(aNum):
    x = 1
    space = 2*aNum-3
    while x < aNum:
        print(str(x)*x+" "*space+str(x)*x)
        x = x + 1
        space = space -2
    if x == aNum:
        y = aNum*2-1
        print(str(x)*y)
        print(str(x)*y)
    space = 1
    while aNum >= 1:
        aNum = aNum - 1
        print(str(aNum)*aNum+" "*space+str(aNum)*aNum)
        space = space + 2


def printTimes(start,end,inc):
    print("Times:",end = "\t")
    for x in range (start,end,inc):
        print(x, end = "\t")
    print("")
    for x in range(start,end,inc):
        print(x, end = "\t")
        for y in range(start,end,inc):
            print(x*y, end = "\t")
        print("")












