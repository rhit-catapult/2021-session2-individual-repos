import pygame, sys


class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   has_exploded to False.
        self.screen = screen
        self.x = x
        self.y = 591
        self.has_exploded = False

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        self.y = self.y - 5

    def draw(self):
        # Draw a vertical, 4 pixels thick, 8 pixels long, red (or green) line on the screen,
        # where the line starts at the current position of this Missile.
        pygame.draw.line(self.screen, (150, 255, 0), (self.x, self.y), (self.x, self.y + 5), 2)


class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed)
        self.screen = screen
        self.y = y
        self.x = x
        self.missiles = []
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey((255, 255, 255))

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(pygame.image.load("fighter.png"), (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        new_missile = Missile(self.screen, self.x + 50)
        self.missiles.append(new_missile)

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same name.
        # Set   is_dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        is_dead = False
        original_x = x
        move_right = True
        pygame.image.load("badguy.png")
        self.image = pygame.image.load("badguy.png")
        self.image.set_colorkey((0, 0, 0))

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        pass

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        pass

    def hit_by(self, missile):
        # Make a Badguy hitbox rect.
        badguy_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        # Return True if that hitbox collides with the xy point of the given missile.
        return badguy_hitbox.collidepoint(missile.x, missile.y)



class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        pass

    def move(self):
        # Make each badguy in this EnemyFleet move.
        pass

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        pass

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # 9: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3
    # 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    # 1: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # TODO 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.KEYDOWN:
                if pressed_keys[pygame.K_SPACE]:
                    fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # 3: If pygame.K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5


        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x -= 5
    # 4: If pygame.K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < 590:
            fighter.x += 5

        # 2: Draw the fighter
        fighter.draw()
        # 11: Move the enemy_fleet
        enemy_fleet.move()
        # 12: Draw the enemy_fleet
        enemy_fleet.draw()
        # TODO 6: For each missile in the fighter missiles
        for missile in fighter.missiles:
            missile.draw()
            missile.move()
        #   TODO 7: Move the missile
        #   TODO 8: Draw the missile

        # TODO 12: For each badguy in the enemy_fleet.badguys list


        #     TODO 13: For each missile in the fighter missiles
        #         TODO 14: If the badguy is hit by the missile
        #             TODO 15: Mark the badguy is_dead = True
        #             TODO 16: Mark the missile has_exploded = True

        # TODO 17: Use the fighter to remove exploded missiles
        # TODO 18: Use the enemy_fleet to remove dead badguys

        # TODO 19: If the enemy is_defeated
        #     TODO 20: Increment the enemy_rows
        #     TODO 21: Create a new enemy_fleet with the screen and enemy_rows

        # TODO 22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score

        # TODO 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
