import time
import math
import random

def variables():
    print("\n---Variables---")
    x = 7
    myName = "Alexander"
    print(x + 3, myName)

def strings():
    print("\n---strings---")
    doubles = "Yes, that's correct"
    singles = "this is also correct."
    triples = """even this works"""
    fStrings = f"{doubles}"
    print(doubles)
    print(singles)
    print(triples)
    print(fStrings)

def loops():
    print("\n---loops---")
    total = 0
    for k in range(5):
        total += k
    print(total)

    x = 0
    while True:
        print(x)
        x += 1

        if x > 6:
            break

def sequences():
    print("\n---Sequences---")
    myList = [4, 5, 6, 7]
    for k in range(len(myList)):
        print("Index:", k, "Value:", myList[k])
    for value in myList:
        print("Value:", value)

    myTuple = (0, 1, 2, 3)
    print(myTuple[0])

def functions(number1, number2, number3):
    print("\n---functions---")
    print(number1 + number2, number3)
    return number1 * number2
    #anything beyond this point will not run

def imports():
    print("\n ---imports---")
    print(math.cos(1))
    print(random.randrange(1, 100))

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        t = self.x
        self.x = self.y
        self.y = t

def classes():
    print("\n ---classes---")
    p1 = Point(3, 4)
    p2 = Point(11, 22)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    p2.swap()
    print(p1.x, p1.y, p2.x, p2.y)

def main():
    print("Hello, world!")
    variables()
    strings()
    loops()
    sequences()
    functions(1, 2, 3)
    imports()
    classes()

main()
