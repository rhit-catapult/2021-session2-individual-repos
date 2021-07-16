import math
import random

def variables():
    print("\n--- Variables ---")
    x=7
    my_name = "Caleb"
    print(x+3, my_name)

def Strings():
    print("\n--- Strings ---")
    doubles = "Double quotes work."
    singles = 'Single quotes work.'

def loops():
    print("\n--- Loops ---")
    total=0
    for k in range(5):
        total = total+k

    print(total)

    x=0
    while True:
            x=x+1
            print(x)
            if x>6:
                break

def sequences():
    print("\n--- Sequences ---")
    my_list = [4,5,6,7]
    print(my_list[1])
    my_list[3] = "Bob"
    print(my_list)
    print(len(my_list))
    for k in range(len(my_list)):
        print("Index",k, "Values", my_list[k])

    my_tuple=(8,9,10,11)
    print(len(my_tuple))
    for k in range(len(my_tuple)):
        print("Index", k, "Values", my_tuple[k])

def functions(number1, number2, name):
    print("\n--- Functions ---")
    print(number1+number2)

def imports():
    print("\n---Imports---")
    print(math.cos(0))
    print(random.randrange(1,10))
    print(math.pi)

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def swap(self):
        t=self.x
        self.x=self.y
        self.y=t

def classes():
    print("\n---Classes---")
    p1=Point(3,4)
    p2=Point(11,12)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    print(p1.x, p1.y, p2.x, p2.y)



def main():
    print("Hello, World!")
    variables()
    Strings()
    loops()
    sequences()
    functions(3,4,"Bob")
    imports()
    classes()

main()