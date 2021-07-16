# FIRST CATAPULT PYTHON LECTURE FROM DR. FISHER--Day 3

import math
import random


def variables():
    print("\n--- Variables ---")
    x = 7
    my_name = "Tristen"
    print(x + 3, my_name * 5)


def strings():
    print("\n--- Strings ---")
    doubles = "Double quotes work"
    singles = 'Single quotes work too'
    triples = """Triple quotes work as well, but they're weird"""
    a = 77
    f_strings = f"Allow {a} in-line variables {2 * a}"
    # f stands for "formatted string"
    print(doubles)
    print(singles)
    print(triples)
    print(f_strings)


def loops():
    print("\n--- Loops ---")
    total = 0
    # range is a command that makes a list (starting with 0)
    for k in range(5):
        # total = total + k can be written as:
        total += k
    print(total)
    # Why does it print out 10?

    x = 0
    while True:
        x = x + 1
        print(x)
        if x > 6:
            break


def sequences():
    print("\n--- Sequences ---")
    # Python calls it "sequences", a lot of other languages call them "arrays"
    my_list = [4, 5, 6, 7]
    # list is 0 based (4 is item 0, 5 is item 1, etc.)
    print(my_list[1])
    # Lists are modifiable
    my_list[3] = "Bob"
    print(my_list)

    # iterate via an index
    print(len(my_list))
    for k in range(len(my_list)):
        print("Index", k)
        print("Index", k, "Values", my_list[k])

    # iterate via an index
    for value in my_list:
        print("Value", value)

    # another sequence is a tuple (like a list, but CAN'T be modified)
    my_tuple = (8, 9, 10, 11)
    print(my_tuple[0])



def functions(number1, number2, name):
    print("\n--- Functions ---")
    print(number1 + number2)
    print(name)
    return number1 * number2
    # Code after "return" doesn't run
    print("This code does NOT run")


def imports():
    # Using someone else's code
    print("\n--- Imports ---")
    print(math.pi)
    print(math.cos(2.5))
    print(random.randrange(1, 100))


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 'Swap' is a method
    def swap(self):
        # Use temporary variable to not replace a variable
        t = self.x
        self.x = self.y
        self.y = t



def classes():
    # Purely for exposure, don't have to internalize/be good at
    print("\n--- Classes ---")
    p1 = Point(3,4)
    p2 = Point(11, 22)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    print(p1.x, p1.y, p2.x, p2.y)



def main():
    print("Hello world")
    variables()
    strings()
    loops()
    sequences()
    functions(3, 4, "Bob")
    y = functions (3, 4, "Bob")
    print(y)
    imports()
    classes()



main()

