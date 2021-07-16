import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, color,x, y,radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        color1 = random.randrange(0, 255)
        color2 = random.randrange(0, 255)
        color3 = random.randrange(0, 255)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y

        if self.x > self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.x < 0:
            self.speed_x = -self.speed_x
        if self.y > self.screen.get_height():
            self.speed_y = -self.speed_y
        if self.y < 0:
            self.speed_y = -self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # color1 = random.randrange(0, 255)
    # color2 = random.randrange(0, 255)
    # color3 = random.randrange(0, 255)
    # color4 = random.randrange(0, 255)
    # color5 = random.randrange(0, 255)
    # color6 = random.randrange(0, 255)
    # TODO: Create an instance of the Ball class called ball1
    ball1 = Ball(screen, (0,0,0), 150,150,10, 10, 5)
    ball2 = Ball(screen, (0,0,0), 100, 100, 10,-10, 5)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        ball1.move()
        ball2.move()

        # TODO: Draw the ball
        ball1.draw()
        ball2.draw()


        pygame.display.update()


main()


# Optional challenges (if you finish and want to play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
