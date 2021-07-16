import math
import random



def main():
    print("\nHello, World!")
    variables()
    strings()
    loops()
    sequences()
    functions(3, 4, "bob") #functions can recieve
    y = functions(3, 4, "bob")
    print(y)
    imports()
    classes()



def variables():
    print("\n--- Variables ---")
    x = 7
    cat_name = "Fluffy "
    print(x + 2, cat_name * 10)


def strings():
    print("\n --- Strings ---")
    doubles = "double quotes work"
    single = 'single quotes work too'
    triple = """triple quotes work too"""
    a = 77
    f_strings = f"Allow {a} inline variables {2 * a}"
    print(doubles + single + triple)
    print (f_strings)

def loops():
    print("\n --- Loops ---")
    total = 0
    for k in range(5): #k = 0, 1 , 2 , 3 , 4
        #total += k
        total = total + k
    print(total)

    x = 0
    while True:
        x = x + 1
        print(x)
        if x > 6:
            break

def sequences():
    print("\n --- Sequences ---")
    my_list = [4, 5, 6, 7]
    print(my_list[1]) # prints 5
    my_list[3] = "bob"
    # my_list[4] would crash
    print(my_list)
    my_list[3] = 7

    # iterate via an index
    print(len(my_list))
    for k in range (len(my_list)):
        print("Index", k, "Value", my_list[k])

    # iterate via values (enhanced for loop)
    for value in my_list:
        print("Value", value)

    # Another sequence is a Tuple
    my_tuple = (8, 9 , 10, 11)
    print(my_tuple[0])
    # a tuple can't be modified or changed unlike a list

def functions(number1, number2, name):
    print("\n ---Functions---")
    print(number1 + number2)
    print(name)
    return number1 * number2

def imports():
    print("\n ---Imports---")
    print(math.pi)
    print(math.cos(2.5))
    print(random.randrange(1, 100)) # random number


class Point():

    def __init__(self, x, y): # init initializes
        self.x = x
        self.y = y

    def swap(self):
        t = self.x
        self.x = self.y
        self.y = t

def classes():
    print("\n ---Classes---")
    p1 = Point(3, 4)
    p2 = Point(11, 22)
    print(p1.x, p1.y, p2.x, p2.y)
    p1.swap()
    print(p1.x, p1.y, p2.x, p2.y)


main()




