# Kwang Su Choi & Rachael DePriest
# CS 1301 B5
# Kwang Su Choi (902969968) & Rachael DePriest (902906726)
# kchoi20@gatech.edu & rdepriest3@gatech.edu
# We worked on this homework assignment alone, using only this semester's course materials.


from Myro import*

init()

def actingCode():
    acting = True
    direction = input("L = left, R = right, F = forward, B = back, S = stop")
    while acting == True:
        if direction == "L":
            turnLeft(1,0.5)
            stop()
            direction = input("L = left, R = right, F = forward, B = back, S = stop")
        elif direction == "R":
            turnRight(1,0.5)
            stop()
            direction = input("L = left, R = right, F = forward, B = back, S = stop")
        elif direction == "F":
            forward(1,0.5)
            stop()
            direction = input("L = left, R = right, F = forward, B = back, S = stop")
        elif direction == "B":
            backward(1,0.5)
            stop()
            direction = input("L = left, R = right, F = forward, B = back, S = stop")
        elif direction == "S":
            stop()
            return


