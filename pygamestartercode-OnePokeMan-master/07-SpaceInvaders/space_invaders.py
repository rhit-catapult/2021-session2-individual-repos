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
        self.y -= 5

    def draw(self):
        # Draw a vertical, 4 pixels thick, 8 pixels long, red (or green) line on the screen,
        # where the line starts at the current position of this Missile.
        shoot_sound = pygame.mixer.Sound("pew.wav")
        shoot_sound.play()
        pygame.draw.line(self.screen, pygame.Color("Green"), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed)
        self.screen = screen
        self.x = x
        self.y = y
        self.missiles = []
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey(pygame.Color("White"))

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        fired_missile = Missile(self.screen, self.x + 50)
        self.missiles.append(fired_missile)

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
        self.is_dead = False
        self.original_x = x
        self.move_right = True
        self.image = pygame.image.load("badguy.png")
        self.image.set_colorkey(pygame.Color("Black"))

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        self.x += self.speed
        if self.x > self.original_x + 100 or self.x < self.original_x - 100:
            self.speed *= -1

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
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
        if not self.badguys:
            return True
        else:
            return False

    def move(self):
        # Make each badguy in this EnemyFleet move.
        for each in self.badguys:
            each.move()

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        for each in self.badguys:
            each.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = 30

    def draw(self, x, y):
        font = pygame.font.Font(None, self.font)
        text = f"Score: {self.score}"
        caption = font.render(text, True, pygame.Color("White"))
        self.screen.blit(caption, (x, y))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))
    over_image = pygame.image.load("gameover.png")
    scoreboard = Scoreboard(screen)
    enemy_death_sound = pygame.mixer.Sound("explosion.wav")
    win_sound = pygame.mixer.Sound("win.wav")
    lose_sound = pygame.mixer.Sound("lose.wav")

    # DONE 9: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3
    # DONE 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    # DONE 1: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # DONE 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # DONE 3: If pygame.K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5
        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x -= 5
        # DONE 4: If pygame.K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < 590:
            fighter.x += 5
        # DONE 2: Draw the fighter
        fighter.draw()

        # DONE 11: Move the enemy_fleet
        enemy_fleet.move()
        # DONE 12: Draw the enemy_fleet
        enemy_fleet.draw()
        # DONE 6: For each missile in the fighter missiles
        for missile in fighter.missiles:
        #   DONE 7: Move the missile
            missile.move()
        #   DONE 8: Draw the missile
            missile.draw()

        # DONE 12: For each badguy in the enemy_fleet.badguys list
        for guy in enemy_fleet.badguys:
        #     DONE 13: For each missile in the fighter missiles
            for missile in fighter.missiles:
        #         DONE 14: If the badguy is hit by the missile
                if guy.hit_by(missile):
                    enemy_death_sound.play()
                    scoreboard.score += 100
        #             DONE 15: Mark the badguy is_dead = True
                    guy.is_dead = True
        #             DONE 16: Mark the missile has_exploded = True
                    missile.has_exploded = True

        # DONE 17: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missiles()
        # DONE 18: Use the enemy_fleet to remove dead badguys
        enemy_fleet.remove_dead_badguys()
        # DONE 19: If the enemy is_defeated
        if enemy_fleet.is_defeated:
            win_sound.play()
        #     DONE 20: Increment the enemy_rows
            enemy_rows += 1
        #     DONE 21: Create a new enemy_fleet with the screen and enemy_rows
            enemy_fleet = EnemyFleet(screen, enemy_rows)
        # DONE 22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)
        for guy in enemy_fleet.badguys:
            if guy.y > 545:
                game_over = True
                if game_over:
                    lose_sound.play()
                    screen.blit(over_image, (170, 200))

        # DONE 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score
        scoreboard.draw(5, 5)

        # DONE 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
