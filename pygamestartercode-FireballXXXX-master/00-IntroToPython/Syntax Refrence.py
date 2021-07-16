import math
import random

def variables():
    print("\n--- Variables ---")
    x = 7
    my_name = "Noah"
    print(x + 3, my_name * 5)


def strings():
    print("\n---Strings---")
    doubles = "Double quotes works"
    singles = "Single quotes works"
    triples = """Allow
    crazy
    formatting!"""
    a = 77
    f_strings = f"Allow {a} inline variables {2 * a}"


def loops():
    print("\n---Loops---")
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
    print("\n---Sequences---")
    my_list = [4, 5, 6, 7]
    print(my_list[1])
    my_list[3] = "Bob"
    print(my_list)

    # iterate via an index
    print(len(my_list))
    for k in range(len(my_list)):
        print("index", k, "Value", my_list[k])

    # iterate via values
    for value in my_list:
        print("Value", value)

    # Another sequence is a Tuple
    my_tuple = (8, 9, 10, 11)
    print(my_tuple[0])


def functions(number1, number2, name):
    print("\n---Functions---")
    print(number1 + number2)
    print(name)
    return number1 + number2


def imports():
    print("\n---Imports---")
    print(math.pi)
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
    print("\n---classes---")
    p1 = Point(3, 4)
    p2 = Point(11, 22)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    print(p1.x, p1.y, p2.x, p2.y)


def main():
    print("Hello World!")
    variables()
    strings()
    strings()
    loops()
    sequences()
    functions(3, 4, "Bob")
    imports()
    classes()


main()
