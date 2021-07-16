import math;
import random;

def variables():
    print("\n--- Variables ---");
    x = 7;
    my_name = "blickuh"
    print(x + 3, my_name * 5);

def strings():
    print("\n--- Stringz ---");
    doubles = "Double quotes work.";
    singles = 'Single quotes work too!';
    triples = """Triples
    Allow
    Crazy
    Formatting""";
    a = 77;
    f_strings = f"Allow {a} inline variables {2 * a}";
    print(doubles);
    print(singles);
    print(triples);
    print(f_strings);

def loops():
    print("\n--- Loops ---");
    total = 0;
    for k in range(5):
        total = total + k;
    print(total);

    x = 0;
    while True:
        x = x + 1;
        print(x);
        if x > 6:
            break;


def sequences():
    print("\n--- Sequences ---");
    my_list = [4, 5, 6, 7];
    print(my_list[1]);
    my_list[3] = "Bob";
    # my_list[4] = "Bob" would crash, out of bounds
    print(my_list);


    #Iterate via an index
    print(len(my_list));
    for k in range(len(my_list)):
        print("Index", k, "Values", my_list[k]);


    # Enhanced For Loop
    for value in my_list:
        print("Value", value);

    # Another sequences is a Tuple
    my_tuple = (8, 9, 10, 11);
    print(my_tuple[0]);


def functions(number1, number2, name):
    print("\n--- Functionz ---");
    print(number1 + number2);
    print(name);
    return number1 * number2;
    print("This code does NOT run");
    #Code after return statement doesn't runn


def imports():
    print("\n--- Imports ---");
    print(math.pi);

class Point():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def swap(self):
        t = self.x;
        self.x = self.y;
        self.y = t;

def classes():
    print("\n--- Classes ---");
    p1 = Point(3, 4);
    p2 = Point(11, 22);
    print(p1.x, p1.y, p2.x, p2.y);
    p1.swap;
    print(p1.x, p1.y, p2.x, p2.y);



def main():
    print("Hello, World!");
    variables();
    strings();
    loops();
    sequences();
    y = functions(3, 4, "Bob");
    print(y);
    imports();
    classes();


main()
