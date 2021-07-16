import pygame
import sys
import time
import random
clock = pygame.time.Clock()

class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randrange(5, 15)

    def move(self):
        self.y = self.y + self.speed

    def off_screen(self):
        return (self.y > self.screen.get_height() + 10)
        
    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 4), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_without_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
        pass

    def draw(self):
        self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        if time.time() > self.last_hit_time + 0.5:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        hero_hit_box = pygame.Rect(self.x, self.y, self.image_with_umbrella.get_width(), self.image_with_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        new_raindrop = Raindrop(self.screen, self.x + random.randrange(0, 300), self.y + 100)
        self.raindrops.append(new_raindrop)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike's rainy day'")
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")
    cloud = Cloud(screen, 300, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            cloud.x = cloud.x + 5
        if pressed[pygame.K_a]:
            cloud.x = cloud.x - 5
        if pressed[pygame.K_s]:
            cloud.y = cloud.y + 5
        if pressed[pygame.K_w]:
            cloud.y = cloud.y - 5

        screen.fill((255, 255, 255))

        cloud.draw()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)
        mike.draw()
        pygame.display.update()

main()
