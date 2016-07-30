#Kwang Su Choi
#CS 1301 B5
#902969968
#kchoi20@gatech.edu
#I,Kwang Su Choi, have worked on this assignment using https://docs.python.org/2/library/time.html for time.sleep function.

## My program will automatically convert how much American dollar you have in your pocket into other countries' currency.
## It will ask you some questions and at the end it will provide the calculated currency for the country that you want to go visit.
## At first, I just made it calculate the currency, but then I thought it would be too simple so I added extra information to make it more elaborate.
## I added famous tourist destinations to go visit with that converted money, so it is more useful than just converting currency.
## I am sure that there is an app for this, but I wanted to make it my own version by myself so that is my aspiration for this project.
## I do not have all the countries in the world in this program but it has most of the major countries in the world so it is quiet useful when you are traveling around the world and don't have to google it everytime.

import time


def convertMyDollar():


    input1 = float(input("How much do you have in dollar? $"))
    input2 = input("In which country that you want to convert your dollar into? \n (Don't forget to capitalize the first letter of a country!)")

    f = open("countries.txt")
    countries = f.readlines()

    if input2 == "Congo":
        congo = float(input1*925)
        print("Your $",input1,"will be worth",congo,"franc.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Congo":
                    print("You should go visit",element2)
    elif input2 == "Ghana":
        ghana = float(input1*2.7625)
        print("Your $",input1,"will be worth",ghana,"cedi.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Ghana":
                    print("You should go visit",element2)
    elif input2 == "Kenya":
        kenya = float(input1*86.81)
        print("Your $",input1,"will be worth",kenya,"shilling.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Kenya":
                    print("You should go visit",element2)
    elif input2 == "Madagascar":
        mada = float(input1*0.72)
        print("Your $",input1,"will be worth",mada,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Madagascar":
                    print("You should go visit",element2)
    elif input2 == "Nigeria":
        nigeria = float(input1*162.27)
        print("Your $",input1,"will be worth",nigeria,"naira.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Nigeria":
                    print("You should go visit",element2)
    elif input2 == "South Africa":
        sa = float(input1*10.51)
        print("Your $",input1,"will be worth",sa,"rand.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "South Africa":
                    print("You should go visit",element2)
    elif input2 == "China":
        china = float(input1*6.23)
        print("Your $",input1,"will be worth",china,"yuan.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "China":
                    print("You should go visit",element2)
    elif input2 == "India":
        india = float(input1*60.59)
        print("Your $",input1,"will be worth",india,"rupee.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "India":
                    print("You should go visit",element2)
    elif input2 == "Japan":
        japan = float(input1*102.63)
        print("Your $",input1,"will be worth",japan,"yen.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Japan":
                    print("You should go visit",element2)
    elif input2 == "South Korea":
        sk = float(input1*1039.01)
        print("Your $",input1,"will be worth",sk,"won.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "South Korea":
                    print("You should go visit",element2)
    elif input2 == "Taiwan":
        taiwan = float(input1*0.033)
        print("Your $",input1,"will be worth",taiwan,"taiwan dollar.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Taiwan":
                    print("You should go visit",element2)
    elif input2 == "Afghanistan":
        afgh = float(input1*0.01)
        print("Your $",input1,"will be worth",afgh,"afghan afghani.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Afghanistan":
                    print("You should go visit",element2)
    elif input2 == "Iraq":
        iraq = float(input1*0.00086)
        print("Your $",input1,"will be worth",iraq,"Iraqi dinar.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Iraq":
                    print("You should go visit",element2)
    elif input2 == "Israel":
        israel = float(input1*0.29)
        print("Your $",input1,"will be worth",israel,"sheqel.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Israel":
                    print("You should go visit",element2)
    elif input2 == "Syria":
        syria = float(input1*0.0068)
        print("Your $",input1,"will be worth",syria,"Syrian pound.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Syria":
                    print("You should go visit",element2)
    elif input2 == "Australia":
        aust = float(input1*0.94)
        print("Your $",input1,"will be worth",aust,"Australian dollar.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Australia":
                    print("You should go visit",element2)
    elif input2 == "New Zealand":
        nz = float(input1*0.86)
        print("Your $",input1,"will be worth",nz,"New Zealand dollar.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "New Zealand":
                    print("You should go visit",element2)
    elif input2 == "France":
        euro = float(input1*0.72)
        print("Your $",input1,"will be worth",euro,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "France":
                    print("You should go visit",element2)
    elif input2 == "Germany":
        euro = float(input1*0.72)
        print("Your $",input1,"will be worth",euro,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Germany":
                    print("You should go visit",element2)
    elif input2 == "Greece":
        euro = float(input1*0.72)
        print("Your $",input1,"will be worth",euro,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Greece":
                    print("You should go visit",element2)
    elif input2 == "Italy":
        euro = float(input1*0.72)
        print("Your $",input1,"will be worth",euro,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Italy":
                    print("You should go visit",element2)
    elif input2 == "Portugal":
        euro = float(input1*0.72)
        print("Your $",input1,"will be worth",euro,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Portugal":
                    print("You should go visit",element2)
    elif input2 == "Spain":
        euro = float(input1*0.72)
        print("Your $",input1,"will be worth",euro,"euro.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Spain":
                    print("You should go visit",element2)
    elif input2 == "Russia":
        russia = float(input1*35.73)
        print("Your $",input1,"will be worth",russia,"ruble.")
        time.sleep(1.5)
        input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
        if input3 == "yes":
            for item in countries:
                y = item.split(",")
                element1 = y[0]
                element2 = y[1]
                if element1 == "Russia":
                    print("You should go visit",element2)
    elif input2 == "United Kingdom":
            uk = float(input1*0.6)
            print("Your $",input1,"will be worth",uk,"pound.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "United Kingdom":
                        print("You should go visit",element2)
    elif input2 == "Argentina":
            argentina = float(input1*8)
            print("Your $",input1,"will be worth",argentina,"peso.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Argentina":
                        print("You should go visit",element2)
    elif input2 == "Brazil":
            brazil = float(input1*2.24)
            print("Your $",input1,"will be worth",brazil,"Brazilian real.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Brazil":
                        print("You should go visit",element2)
    elif input2 == "Colombia":
            colombia = float(input1*1918.95)
            print("Your $",input1,"will be worth",colombia,"peso.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Colombia":
                        print("You should go visit",element2)
    elif input2 == "Uruguay":
            uruguay = float(input1*22.92)
            print("Your $",input1,"will be worth",uruguay,"peso.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Uruguay":
                        print("You should go visit",element2)
    elif input2 == "Venezuela":
            venezuela = float(input1*6.29)
            print("Your $",input1,"will be worth",venezuela,"bolivar.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Venezuela":
                        print("You should go visit",element2)
    elif input2 == "Canada":
            canada = float(input1*1.10)
            print("Your $",input1,"will be worth",canada,"Canadian dollar.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Canada":
                        print("You should go visit",element2)
    elif input2 == "Honduras":
            honduras = float(input1*19.11)
            print("Your $",input1,"will be worth",honduras,"lempira.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Honduras":
                        print("You should go visit",element2)
    elif input2 == "Jamaica":
            jamaica = float(input1*110.09)
            print("Your $",input1,"will be worth",jamaica,"Jamaican dollar.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Jamaica":
                        print("You should go visit",element2)
    elif input2 == "Mexico":
            mexico = float(input1*13.03)
            print("Your $",input1,"will be worth",mexico,"peso.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Mexico":
                        print("You should go visit",element2)
    elif input2 == "Cuba":
            cuba = float(input1*26.5)
            print("Your $",input1,"will be worth",cuba,"peso.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Cuba":
                        print("You should go visit",element2)
    elif input2 == "Haiti":
            haiti = float(input1*44.89)
            print("Your $",input1,"will be worth",haiti,"gourde.")
            time.sleep(1.5)
            input3 = input("Now you have converted your money, let's go spend that money! \n 1. Do you want to know the famous tourist spots in that country? (yes or no) \n 2. Or just type 'quit' if you want to stop using this program.")
            if input3 == "yes":
                for item in countries:
                    y = item.split(",")
                    element1 = y[0]
                    element2 = y[1]
                    if element1 == "Haiti":
                        print("You should go visit",element2)


    elif input2 not in countries:
        input3 = input("Your country is not in the list. You might want to go google that for yourself. \n Do you want to try for another country? Or if you want to quit, just type 'quit'.")
        if input3 == "quit":
            print("Thank you for using this program! \n Have a great day!")
        else:
            convertMyDollar()



    f.close





