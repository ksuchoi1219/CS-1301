#Kwang Su Choi & Brian Bradley
#CS 1301 B5
#Kwang Su Choi (902969968) & Brian Bradley (902955107)
#kchoi20@gatech.edu & bbradley2013@gatech.edu
#We worked on this homework assignment alone, using only this semester's course materials.


def currency(x):
    dollars = float (x)
    dirhams = x/.27
    return dirhams


def puppies(x):
    seeds = x
    minimum = int(2*x)
    maximum = int (5*x)
    print ("You can get a minimum of",minimum,"puppies and a maximum of",maximum,"puppies with",seeds,"magical seeds.")


def teaParty(x):
    people = x
    ounces = x/3
    print ("You should buy {:.3f}".format(ounces),"ounces of tea.")


def moneyLeft(x):
    x = float (x)
    rent = .2*x
    food = .35*x
    money = x-(rent+food)
    print ("You have {:.2f}".format(money),"dollars left to spend.")

import math

def batteriesCalculator():
    response = int(input ("How many orbits would they be in space?"))
    hours = response * 1.51659999913
    batteries = hours / 9
    print (batteries)
    print ("You will need to bring",int (math.ceil(batteries)),"batteries to last",response,"orbits.")
    return int(math.ceil(batteries))





