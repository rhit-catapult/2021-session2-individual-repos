import math
import random

def variables():
    print("/n---Variables---")
    x = 7
    my_name = "Spencer"
    print(x + 3, my_name * 10)

def strings():
    print("/n---Strings---")

def main():
    print("Hello, World!")
    variables()
    strings()
    loops()
    sequences()

    y = functions(3, 4, "Bob")
    print (y)
    singles = 'singles quotes are allowed'
    doubles = "obviously works"
    triples = """allow crazy formating"""
    a = 77
    f_strings = f"allow {a} inline variables {2 * a}"
    print(singles)
    print(doubles)
    print(triples)
    print(f_strings)


def loops():
    print("/n---loops---")
    total = 0
    for k in range(5):
        #total = total + k
        total += k
    print(total)

    x = 0
    while True:
        x = x + 1
        print(x)
        if x > 6:
                break

def sequences():
    print("/n---Sequences---")
    my_list = [4, 5, 6, 7,]
    print(my_list[0])
    my_list[1] = "Bob"
    #my_list[4] = "Bob" would crash
    print(my_list)

    print(len(my_list))
    for k in range(len(my_list)):
        print("Index", k, "Values", my_list[k])

    for values in my_list:
        print("Values", values)

    my_tuple = (8, 9, 10, 11,)
    print(my_tuple[0])
    # my_tuple[3] =

def functions():
    name = Spencer
    number1 = 1
    number2 = 2
    print("/n---Function---")
    print(number1 + number2)
    print(name)
    return number1 * number2
    print("this code does not run")


def imports():
    print("---Imports---")
    print(math.pi)
    print(math.cos(2.5))
    print(random.randrange(1, 100))

class point():

    def _init_(self, x, y,):
        self.x = x
        self.y = y

    def swap(self):
        t = self.x
        self.x = self.y
        self.y = t

def classes():
    print("/n---Classes---")
    p1 = Point(3, 4)
    p2 = Point(11,22)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    print(p1.x, p1.y, p2.x, p2.y,)

main()