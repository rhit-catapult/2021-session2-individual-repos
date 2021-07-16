# Intro to Python (00)
    # 00 Comments, Strings, and Print
        # how to print simple strings/calculations using the "print" command
    # 01 Expressions
        # Part 1: Numbers, Arithmetic, and Precedence (Order of Operations)
            # Write a statement that prints my name
print("Tristen Shields")
            # Type out simple calculations (addition, subtraction, multiplication, division)
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
            # Python follows PEMDAS (order of operations
print(4 + 2 * 2)
            # ** will perform exponentials
print(2 ** 3)
        # Part 2: Exceptions: Syntax and Run-Time Errors
            # what syntax errors look like
        # Part 3: Objects, Types, and Values
            # Using the type() command to figure out the type of an object
                # Int = integers/whole numbers
                # Float = decimal numbers ("floating point number")
                # Str = strings/messages (in quotes)
                # List = [1, 2, 3, 4]
                # Tuple = (1, 2, 3, 4)
                # There are also built in functions/methods, which is its own type
            # When dividing, there is always at least one place past the decimal + follows sig figs (or so it seems)
            # // means integer division WITHOUT the remainder
print(17 // 5)
            # % means integer division ONLY GIVING the remainder
print(17 % 5)
            # '+' and '-' operators also work on strings
print("Hello" + " there")
            # You can either use '', "", or """ """ for strings/messages/text
        # Part 4: Names, Variables, and Assignment
            # You can assign variables using the single '=' sign
            # You can't:
                # Add numbers to a string
                # Take the square root of a negative number
                # Divide by zero
            # You can't assign a letter to a number (e.g. 45 = a)
            # You can keep changing the same variable (e.g. repeatedly adding +1 to x)
    # 02 'Todo' and Commit Push
        # Putting a '#' in front of code makes the program ignore it, making it a note
        # Each blue bar on the right hand side indicates a 'TODO' in the module
        # If the font of the file/module is BLUE it means changes have been made that haven't been pushed to the cloud
        # COMMIT AND PUSH FREQUENTLY FOR EVERY MODULE
    # 03 Names and Expressions
        # You can do advanced math functions in Python by importing the library 'math' ("import math")
    # 04 Functions
        # You know this pretty well, but you can define objects in functions
            # (e.g. in main, say hello("Snow White"), but define the function as hello(friend)
            # This defines "Snow White" as "friend" in the function)
    # 05 Calling Functions
        # You know how to do this, just put it in main
    # 06 Sequences and Loops
        # Part 1: Sequences
            # A sequence is an ORDERED collection of items, like:
            # Lists, where it can be modified '[]'
list1 = [1, 2, 3, 4]
            # Tuples, where it can't be modified and it's more secure '()'
tuple1 = (1, 2, 3, 4)
            # Append is a method inside the list that allows you to add numbers/items to the list
                # my_list.append(123), for example, adds '123' to the list
list1.append(5)
print(list1)
            # You CAN add strings to lists in addition to numbers
list1.append("bruh")
print(list1)
            # ALL OR MOST SEQUENCES ARE ZERO-BASED
            # You can index lists (getting an item by referring to it's sequence number i.e. [0], [1], [2], etc.)
print(list1[0])
        # Part 2: Loops
            # Use 'for' and 'while' loops to print things in a range
                # (e.g. "for i in range (0, 100): print(i))"
        # Part 3: Loop Over Sequences
            # You can use 'for' loops to print all the elements of a sequence
                # (e.g. "for element in my_list: print(element))
                # Same for a while loop (you'd have to use indexing)
    # 07 Mutation
        # GET HELP WITH 07

# Syntax Reference (lecture)
    # Sequences
        # Use the 'len' (length) function to get the number of items in a list/tuple
            # print(len(my_list))

# Moving Smile (01)
    # pygame.init()
        # initializes pygame
    # pygame.display.set_caption("Moving Smile")
        # sets title of game
    # screen = pygame.set_mode((x, y))
        # creates screen and screen size
    # clock = pygame.time.Clock()
        # creates a system of time
        # clock.tick(fps)
            # fps is an int
    # if event.type == pygame.QUIT:
        #sys.exit()
            # Creates a way to stop the program
    # "While true" = forever loop
    # Pygame events
        # for event in pygame.event.get():
            # if event.type == whatever:
                # pressed_keys = pygame.key.get_pressed
                # if pressed_keys[pygame.K]:
    # Color = screen.fill((R, G, B)
    # pygame.draw.circle(screen, (R, G, B), (x, y), width)
        # Example of drawing a shape in pygame
    # pygame.display.update()
        # Allows code to appear on the created screen

# Dog Bark (02)












