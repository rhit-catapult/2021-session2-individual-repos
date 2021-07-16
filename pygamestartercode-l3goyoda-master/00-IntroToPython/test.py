import math
import random



def variables():
    print("\n--- Variables ---")
    x = 7
    myName = "Dylan"
    print(x + 3, myName)

def strings():
    print("\n--- Strings ---")
    triples = """Cool formatting"""
    print(triples)
    a = 76
    f_strings = f"Allow {a} inline variables {2 * a}"
    print(f_strings)

def loops():
    print("\n--- Loops ---")
    total = 0
    for k in range(5):
        total += k
        #total = total + k
    print(total)

    x = 0
    while True:
        x = x + 1
        print(x)
        if x > 6:
            break

def sequences():
    print("\n--- Sequences ---")
    myList = [4, 5, 6, 7, 8, 9, 34]
    print(myList[2])
    myList[5] = 69
    print(myList)
    
    #iterate, index
    print(len(myList))
    for k in range(len(myList)):
        print("Index", "value =", k)
    
    for value in myList:
        print("Value", value)
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def swap(self):
        t = self.x
        self.x = self.y
        self.y = t

def imports():
    print("\n--- Imports ---")
    print(math.pi)

def classes():
    print("\n--- Classes ---")
    p1 = Point(3, 4)
    p2 = Point(11, 22)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    p2.swap()
    print(p1.x, p1.y, p2.x, p2.y)


def main():
   
    print("Hello World")
    variables()
    strings()
    loops()
    sequences()
    imports()
    classes()
main() 
