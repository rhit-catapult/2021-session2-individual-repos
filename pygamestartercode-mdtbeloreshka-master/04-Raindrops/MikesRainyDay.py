import pygame
import sys
import time  # Note this!
import random  # Note this!

# COURSE OF ACTION NOTES
# raindrop: x, y, screen, needs to be able to draw itself, method to fall (move), needs to destroy itself
# when it hits the bottom (check to see if it's off the screen)
#     draw()
#     move()
#     off.screen()
# hero: x, y, screen, needs to be able to draw itself, needs to know if he's getting hit by the rain
# umbrella y/n), when was he last hit by rain (so that he can switch his
# umbrella/change image to be with or without the umbrella), no movement
#     is_rain_hitting_you.(raindrop
#     image_with_umbrella
#     last_hit_time
#     draw()
#     hit_by(raindrop)
# cloud: x, y, screen, raindrops (maintain a list of the raindrops)
#     draw()
#     rain()
#     move()
#     rain()

class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # TODO 8: Initialize this Raindrop, as follows:

        # TODO    - Store the screen.
        # TODO    - Set the initial position of the Raindrop to x and y.
        # TODO    - Set the initial speed to a random integer between 5 and 15.
        # TODO  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        # screen, x, and y are local variables that go away --> we assign them to something more permanent
        self.speed = random.randrange(5, 15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # TODO 11: Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # TODO 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        if self.y > self.screen.get_height() + 5:
            return True
        else:
            return False

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        pygame.draw.line(self.screen,(50, 50, 200), (self.x, self.y), (self.x, self.y + 5), 2)

        # TODO     from the current position of this Raindrop (use either a black or blue color).


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # TODO 15: Initialize this Hero, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Hero to x and y.
        # TODO    - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        # TODO    - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        # TODO    - Set the "last hit time" to 0.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen= screen
        self.x = x
        self.y = y
        # need to define these for the hero, rain, and cloud every time
        self.image_with_umbrella = pygame.image.load(with_umbrella_filename)
        #
        self.image_without_umbrella = pygame. image.load(without_umbrella_filename)
        #
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:

        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        current_time = time.time()
        if current_time > self.last_hit_time + 1.0:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))
        # the picture will change to the one without the umbrella if more than 1.0 seconds passes without
        # being hit by a raindrop

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # TODO 19: Return True if this Hero is currently colliding with the given Raindrop.
        hero_hit_box = pygame.Rect(self.x, self.y, self.image_with_umbrella.get_width(),
                                   self.image_with_umbrella.get_height())
        # you can break really long lines of text, make sure that indentation is still good
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)
        # will say whether it hits the hero or not

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # TODO 24: Initialize this Cloud, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Cloud to x and y.
        # TODO    - Set the image of this Cloud to the given image filename.
        # TODO    - Create a list for Raindrop objects as an empty list called raindrops.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.cloud_image = pygame.image.load(image_filename)
        self.raindrops = []
        # empty list that's up to us, because there are more than 1

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.cloud_image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # TODO 28: Append a new Raindrop to this Cloud's list of raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        new_raindrop = Raindrop(self.screen, random.randrange(self.x, self.x + 300), self.y + 100)
        # OR
        # new_raindrop = Raindrop(self.screen, random.randrange(self.x, self.x + self.image.get_width()),
        # self.y + self.image.get_height())
        self.raindrops.append(new_raindrop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # TODO 1: Initialize pygame, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    # set the display screen size
    pygame.display.set_caption("Mike's Rainy Day")
    # make the caption

    # TODO 2: Make a Clock
    clock = pygame.time.Clock()
    # make the clock

    # # TODO 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    # test_drop = Raindrop(screen, 320, 10)
    # print(test_drop.x)
    # print(test_drop.y)
    # print(test_drop.speed)
    # # you only write "self" when you're inside the factory

    # TODO 15: Make a Hero, named mike, with appropriate images, starting at position x=300 y=400.
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")

    # TODO 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "cloud.png")
    # make the cloud


    # TODO 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)

        # TODO 4:   Make the pygame.QUIT event stop the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # ability to quit

        # TODO 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        # TODO    Arrange so that the Cloud moves:
        # TODO      5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # TODO      5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        # TODO      5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        # TODO      5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after/outside the events loop.

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 5
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 5
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 5

        # TODO 5: Inside the game loop, draw the screen (fill with white)
        screen.fill(pygame.Color("White"))
        # OR
        # screen.fill((255, 255, 255))
        # make the screen white

        # # TODO 12: As a temporary test, move test_drop
        # test_drop.move()
        # # TODO 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10
        # if test_drop.off_screen():
        #     test_drop.y = 10
        # # TODO 10: As a temporary test, draw test_drop
        # test_drop.draw()
        # # asking the test_drop to draw itself
        # # TODO 20: As a temporary test, check if test_drop is hitting Mike, if so set Mike's last_hit_time
        #
        # if mike.hit_by(test_drop):
        #     mike.last_hit_time = time.time()

        # TODO 26: Draw the Cloud.
        cloud.draw()

        # TODO 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # TODO: Make the Cloud "rain", then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
        #     TODO      - move the Raindrop.
        #     TODO      - draw the Raindrop.
        #     TODO  30: if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
        #     Optional  - if the Raindrop is off the screen or hitting Mike, remove it from the Cloud's list of raindrops.
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        # TODO 18: Draw the Hero
        mike.draw()
        # put here because when rain hits mike, it doesn't disappear, it goes behind him
        # TODO 6: Update the display and remove the pass statement below
        pygame.display.update()

# pass, asks the computer to skip over the function (deleted so that the program can run)

# call main
main()

