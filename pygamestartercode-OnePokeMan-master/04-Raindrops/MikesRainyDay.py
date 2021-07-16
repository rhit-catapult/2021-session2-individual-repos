import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # DONE 8: Initialize this Raindrop, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of the Raindrop to x and y.
        # DONE    - Set the initial speed to a random integer between 5 and 15.
        # DONE  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randrange(5, 15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # DONE 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # DONE 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > 800

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # DONE     from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, pygame.Color("Blue"), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # DONE 16: Initialize this Hero, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of this Hero to x and y.
        # DONE    - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        # DONE    - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        # DONE    - Set the "last hit time" to 0.
        # DONE  Use instance variables:
        # DONE     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        # DONE 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        # DONE    If the current time is greater than this Hero's last_hit_time + 1,
        # DONE      draw this Hero WITHOUT an umbrella,
        # DONE      otherwise draw this Hero WITH an umbrella.
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # DONE 19: Return True if this Hero is currently colliding with the given Raindrop.
        hero_hit_box = pygame.Rect(self.x, self.y, self.image_umbrella.get_width(), self.image_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # DONE 24: Initialize this Cloud, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of this Cloud to x and y.
        # DONE    - Set the image of this Cloud to the given image filename.
        # DONE    - Create a list for Raindrop objects as an empty list called raindrops.
        # DONE  Use instance variables:
        # DONE     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # DONE 28: Append a new Raindrop to this Cloud's list of raindrops,
        # DONE    where the new Raindrop starts at:
        # DONE      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # DONE      - y is this Cloud's y + 100.
        self.raindrops.append(Raindrop(self.screen, random.randrange(self.x, self.x + self.image.get_width()), self.y + self.image.get_height()))

    def move(self, x_delta, y_delta):
        self.x += x_delta
        self.y += y_delta


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # DONE 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("Mike's Rainy Day")
    screen = pygame.display.set_mode((1000, 600))
    # DONE 2: Make a Clock
    clock = pygame.time.Clock()
    # TEMP 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    # DONE 15: Make a Hero, named mike, with appropriate images, starting at position x=300 y=400.
    mike = Hero(screen, 300, 408, "Mike_umbrella.png", "Mike.png")
    # DONE 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "cloud.png")
    # DONE 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:

        clock.tick(60)
        # DONE 4:   Make the pygame.QUIT event stop the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # DONE 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        # DONE    Arrange so that the Cloud moves:
        # DONE      5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # DONE      5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        # DONE      5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        # DONE      5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.
        if event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                cloud.move(0, -10)
            if pressed_keys[pygame.K_DOWN]:
                cloud.move(0, 10)
            if pressed_keys[pygame.K_LEFT]:
                cloud.move(-10, 0)
            if pressed_keys[pygame.K_RIGHT]:
                cloud.move (10, 0)
        # DONE 5: Inside the game loop, draw the screen (fill with white)
        screen.fill(pygame.Color("White"))
        # TEMP 12: As a temporary test, move test_drop
        # TEMP 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10
        # TEMP 10: As a temporary test, draw test_drop
        # TEMP 20: As a temporary test, check if test_drop is hitting Mike, if so set Mike's last_hit_time
        # DONE 22: When you run this test, slow the rain down to a speed of 2 to see the result, then remove that code
        # DONE 26: Draw the Cloud.
        cloud.draw()
        # DONE 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # DONE: Make the Cloud "rain", then:
        # DONE    For each Raindrop in the Cloud's list of raindrops:
        cloud.rain()
        for k in cloud.raindrops:
            # DONE      - move the Raindrop.
            k.move()
            # DONE      - draw the Raindrop.
            k.draw()
            # DONE  30: if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            if mike.hit_by(k):
                mike.last_hit_time = time.time()
            # Optional  - if the Raindrop is off the screen or hitting Mike, remove it from the Cloud's list of raindrops.
            if k.off_screen() or mike.hit_by(k):
                cloud.raindrops.remove(k)
        # DONE 18: Draw the Hero
        mike.draw()

        # DONE 6: Update the display and remove the pass statement below
        pygame.display.update()


main()
