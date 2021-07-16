import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randrange(5,15)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y >= 610


    def draw(self):
        pygame.draw.line(self.screen, (0,0,0), (self.x,self.y), (self.x,self.y-5),2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.imagewithumbrella = pygame.image.load(with_umbrella_filename)
        self.imagewithoutumbrella = pygame.image.load(without_umbrella_filename)
        self.lasthittime = 0

    def draw(self):
        if time.time() >= self.lasthittime + 1:
            self.screen.blit(self.imagewithoutumbrella, (self.x, self.y))
        else:
            self.screen.blit(self.imagewithumbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        herohitbox = pygame.Rect(self.x, self.y,
                                 self.imagewithumbrella.get_width(), self.imagewithumbrella.get_height())
        return herohitbox.collidepoint(raindrop.x,raindrop.y)

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = 500
        self.y =  50
        self.cloud = pygame.image.load(image_filename)
        self.list = []

    def draw(self):
        self.screen.blit(self.cloud,(self.x, self.y))

    def rain(self):
        newraindrop = Raindrop(self.screen, random.randrange(self.x, self.x + 300),
                               self.y + 100)
        self.list.append(newraindrop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike's Rainy Day")

    clock = pygame.time.Clock()
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 500, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_a]:
            cloud.x -= 5
        if pressedkeys[pygame.K_s]:
            cloud.y += 5
        if pressedkeys[pygame.K_w]:
            cloud.y -= 5
        if pressedkeys[pygame.K_d]:
            cloud.x += 5

        screen.fill(pygame.Color("White"))
        #screen.fill((255,255,255))


        cloud.rain()
        for raindrop in cloud.list:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.lasthittime = time.time()
            if raindrop.off_screen():
                cloud.list.remove(raindrop)
        mike.draw()
        cloud.draw()
        pygame.display.update()


main()
