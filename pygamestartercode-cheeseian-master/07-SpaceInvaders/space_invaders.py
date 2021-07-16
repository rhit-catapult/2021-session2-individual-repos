import pygame, sys


class Missile:
    def __init__(self, screen, x):

        self.screen = screen
        self.x = x
        self.y = 591
        self.has_exploded = False

    def move(self):
        self.y -= 5

    def draw(self):
        pygame.draw.line(self.screen, pygame.Color("green"), (self.x, self.y), (self.x, self.y - 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.missiles = []
        self.fighter_image = pygame.image.load("fighter.png")
        self.fighter_image.set_colorkey((255, 255, 255))

    def draw(self):
        self.screen.blit(self.fighter_image, (self.x, self.y))

    def fire(self):
        new_missile = Missile(self.screen, self.x + 50)
        self.missiles.append(new_missile)

    def remove_exploded_missiles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.is_dead = False
        self.original_x = x
        self.move_right = True
        self.image = pygame.image.load("badguy.png")
        self.image.set_colorkey((0, 0, 0))

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        self.x += self.speed


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        badguy_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
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
        for badguys in self.badguys:
            badguys.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    enemy_rows = 3
    enemy_fleet = EnemyFleet(screen, enemy_rows)

    fighter = Fighter(screen, 320, 590)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                fighter.fire()

            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x -= 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < 590:
            fighter.x += 5

        fighter.draw()

        enemy_fleet.move()
        enemy_fleet.draw()

        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        for badguy in enemy_fleet.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.is_dead = True
                    missile.has_exploded = True

        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()

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
