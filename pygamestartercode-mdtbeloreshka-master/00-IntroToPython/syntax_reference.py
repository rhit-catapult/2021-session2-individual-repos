import math
import random

def variables():
    print("\n--- Variables ---")
    # \n makes a new line
    x = 7
    # this is an integer
    my_name = "Maria Denitsa Tsvetanova Beloreshki"
    # this is a string
    print(x + 3, my_name)
    print(x + 5, my_name * 6)

def strings():
    print("\n--- Strings ---")
    doubles = "double quotes work"
    singles = 'single quotes work too'
    triples = """allow crazy formatting"""
    "double quotes work"
    a = 77
    f_strings = f"Allow {a} inline variables {2 * a}"
    print(doubles)
    print(singles)
    print(triples)
    # single, double, and triple quotes all work
    # triple quotes allow for crazy formatting
    # there's no real difference (However, for contractions, use doubles so that the computer knows where the string,
    # etc. ends.)
    # In general, you want to match the style of the code around you.

def loops():
    print("\n--- Loops ---")
    total = 0
    for k in range (5):
        total = total + k
        # OR, total += k
        # prints a list of 0, 1, 2, 3, & 4
    print(total)

    x = 0
    while True:
        x = x + 1
        print(x)
        if x > 6:
            break
            # allows us to break the forever loop

def sequences():
    print("\n--- Sequences ---")
    my_list = [4, 8, 10, 12]
    print(my_list[1])
    my_list[3] = "Bob"
    print(my_list)
    # aka "arrays"

    print(len(my_list))
    # len = length, gives the size of the array
    for k in range(len(my_list)):
        print("Index", k, "Values", my_list[k])

    # iterate via values (enhanced for loop)
    for value in my_list:
        print("Value", value)

    # another sequence is a Tuple
    my_tuple = (4, 5, 6, 7)
    print(my_tuple[3])
    # a tuple is the same as a list, but it cannot be changed
    # tuple is like the cardinality of a list

def functions(humber1, number2, name):
    print("\n--- Functions ---")

    print(number1 + number2)
    print(name)
    # functions can receive things and return them
    return number1 * number2
    print("this code does NOT run!")

def imports():
    print("\n--- Imports ---")
    print(math.pi)
    print(math.cos(1/2))
    print(random.randrange(1, 100))


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        t = self.x
        self.x = self.y
        self.y = t
        # t is a temporary variable here

def classes():
    print("\n--- Classes ---")
    # more advanced part of programming, very popular
    p1 = Point(3, 4)
    # makes a point at (3,4)
    p2 = Point(11, 22)
    # makes a point at (11,22)
    # a class is like a factory, this class is a factory that makes point objects
    print(p1.x, p1.y, p2.x, p2.y)
    # the constructor is the thing that makes the thing "__init__", called a method when it's outside a class
    # the object is called "self"
    # can save data
    p1.swap()
    print(p1.x, p1.y, p2.x, p2.y)

def main():
    print("Hello, World!")
    variables()
    strings()
    loops()
    sequences()
    functions()
    imports()
    classes()
    # the purpose of the colon is to say "here comes the function"
    # indentation is part of the language
    # python is an interpreted language (it runs until in crashes)
    # making a function without calling them is pointless

main()