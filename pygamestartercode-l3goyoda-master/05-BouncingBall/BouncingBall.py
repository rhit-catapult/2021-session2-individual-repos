import pygame
import sys
import random

class Ball():
    def __init__(self, screen, color, x, y, radius, vx, vy):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.image = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball1 = Ball(screen, (0,0,0), 150, 150, 10, 5, 3)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        if ball1.x > 290:
            ball1.vx = ball1.vx * -1
        if ball1.x < 10:
            ball1.vx = ball1.vx * -1
        if ball1.y > 290:
            ball1.vy = ball1.vy * -1
        if ball1.y < 10:
            ball1.vy = ball1.vy * -1

        ball1.x = ball1.x + ball1.vx
        ball1.y = ball1.y + ball1.vy
        ball1.draw()

        pygame.display.update()


main()