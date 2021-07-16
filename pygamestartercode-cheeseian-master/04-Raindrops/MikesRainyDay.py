import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randrange(5, 15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y = self.y + self.speed


    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        return self.y > self.screen.get_height() + 5

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_without_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        current_time = time.time()
        if current_time > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        hero_hit_box = pygame.Rect(self.x, self.y,
                                   self.image_with_umbrella.get_width(), self.image_with_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_cloud = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        new_raindrop = Raindrop(self.screen, random.randrange(self.x, self.x + self.image_cloud.get_width()),
                                random.randrange(self.y + self.image_cloud.get_height() - 20,
                                                 self.y + self.image_cloud.get_height()))
        self.raindrops.append(new_raindrop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("rainyday")
    clock = pygame.time.Clock()

    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 300, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if cloud.x < screen.get_width() - cloud.image_cloud.get_width():
                    cloud.x += 5
            if event.key == pygame.K_LEFT:
                if cloud.x > 0:
                    cloud.x -= 5

        screen.fill((255, 255, 255))

        mike.draw()
        cloud.rain()
        cloud.draw()

        for raindrop in cloud.raindrops:
            raindrop.draw()
            raindrop.move()

            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        pygame.display.update()


main()
