import pygame
import sys
import random


class Ball():
    def __init__(self, screen, x, y, color, speedx, speedy, radius):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.radius = radius
        self.balllist = []
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y),
                           self.radius)
    def move(self):
        if self.x >= 490:
            totalx = -totalx
        if self.x <= 10:
            totalx = -totalx
        if self.y >= 490:
            totaly = -totaly
        elif self.y <= 10:
            totaly = -totaly
        self.y -= totaly
        self.x += totalx
    def instanceball(self):
        newball = Ball(self.screen, random.randrange(50, 950), random.randrange(50, 750), (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), random.randrange(0,5),random.randrange(0,5), 20)
        self.balllist.append(newball)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball1 = Ball(screen, random.randrange(50, 950), random.randrange(50,750), pygame.Color("Blue"), 10, 10, 20)

    totalx = ball1.speedx
    totaly = ball1.speedy
    #     kx = ball1.x - ball1.speedx
    #     jx = ball1.x + ball1.speedx
    #     ky = ball1.y + ball1.speedy
    #     jy = ball1.y - ball1.speedy

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if ball1.x >= 490:
            totalx = -totalx
        if ball1.x <= 10:
            totalx = -totalx
        if ball1.y >= 490:
            totaly = -totaly
        elif ball1.y <= 10:
            totaly = -totaly
        ball1.y -= totaly
        ball1.x += totalx
        clock.tick(60)
        screen.fill(pygame.Color('gray'))


        Ball.instanceball()
        for ball in ball1.balllist:
            ball.draw()
            ball.move()
        # TODO: Move the ball
        # TODO: Draw the ball
        ball1.draw()
        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
