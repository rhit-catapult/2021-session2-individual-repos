# The below two lines constitute what tools we will be using from the toolbox
# that python provides us with. We will be using the pygame tool as well as
# the sys tool. pygame is the big hammer we will use to build our game and
# capture our events (like key presses, mouse movements, etc.). sys is a small
# tool that allows us to communicate with the part of our computer that runs
# python and all other programs!
import pygame
import sys

# Let's turn pygame ON
pygame.init()

# Let's create a caption for the game window
pygame.display.set_caption("Hello World")

# Now the screen is where all the magic is going to happen. Our screen will
# have a width of 640 pixels and a height of 480 pixels. The (0,0) point will
# be at the top left of our screen. 
screen = pygame.display.set_mode((640, 480))

# This is a loop that will run forever, simply because True is always true
while True:
    # Here's another loop inside of the first loop. Notice the indentation,
    # moving one tab width into the while loop makes this statement part of the
    # loop instead of outside of it.
    for event in pygame.event.get():
        # Let's just print all the events that happen in our window, wonder
        # what those could be?
        print(event)

        # we must allow our users to quit the game right? I mean not everyone
        # wants to play forever.
        # This is a conditional statement, i.e., the line sys.exit() will ONLY
        # execute when event.type is equal to pygame.QUIT (this is what ==
        # means). 
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    # Draw things on the screen
    #pygame.draw.circle(screen, color, pos, radius,width)
    #width = outline or not
    #x-y coordinate plane; 0,0 is top left
    pygame.draw.circle(screen, (0,100,255), (0,480), 10)
    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()
