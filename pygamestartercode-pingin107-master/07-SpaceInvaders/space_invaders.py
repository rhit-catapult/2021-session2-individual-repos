import pygame, sys


#  23: Create a Scoreboard class (from scratch)
class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 50)
    def draw(self):
        caption = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(caption, (5,5))


# Hints: Instance variables: screen, score, and font (size 30)
#    Methods: draw (and __init__)
# Create a scoreboard and draw it at location 5, 5
# When a Badguy is killed add 100 points to the scoreboard.score

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
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("fighter.png")
        self.missiles = []
        self.image.set_colorkey((255, 255, 255))
        self.pew = pygame.mixer.Sound("pew.wav")
    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        new_missile = Missile(self.screen, self.x + 50)
        self.missiles.append(new_missile)
        self.pew.play()

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
        self.image = pygame.image.load("badguy.png")
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.is_dead = False
        self.original_x = x
        self.move_right = True

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        """
        if self.move_right:
            self.x += self.speed
            if self.x > self.original_x + 100:
                self.move_right = False
                self.y = self.y + self.speed * 4
        else:
            self.x -= self.speed
            if self.x < self.original_x -100:
                self.y = self.y + self.speed * 4
                self.move_right = True
        """
        #this is the same as the commented lines above but it's shorter
        self.x += self.speed
        if abs(self.x - self.original_x) > 100:
            self.speed = -self.speed
            self.y += abs(self.speed * 4)
    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))


    def hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        enemy_hitbox = pygame.Rect(self.x, self.y,
                                   self.image.get_width(), self.image.get_height())
        return enemy_hitbox.collidepoint(missile.x, missile.y)



class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        self.explode = pygame.mixer.Sound("explosion.wav")
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        if len(self.badguys) == 0:
            return True
        else:
            return False


    def move(self):
        # Make each badguy in this EnemyFleet move.
        for badguy in self.badguys:
            badguy.move()


    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        for badguy in self.badguys:
            badguy.draw()


    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]
                self.explode.play()



def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))
    enemy_rows = 8
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    #  9: Set    enemy_rows    to an initial value of 3.
    #  10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    #  1: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)
    scoreboard = Scoreboard(screen)
    game_over = False
    game_over_sound = pygame.mixer.Sound("lose.wav")
    win_sound = pygame.mixer.Sound("win.wav")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            #  5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_m] or pressed_keys[pygame.K_n]:
                    fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        if game_over:
            game_over_screen = pygame.image.load("gameover.png")
            screen.blit(game_over_screen, (170, 200))
            scoreboard.draw()
            pygame.display.update()
            continue
        pressed_keys = pygame.key.get_pressed()
        #  3: If pygame.K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5
        #  4: If pygame.K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        if pressed_keys[pygame.K_a] and fighter.x > -50:
            fighter.x -= 5

        if pressed_keys[pygame.K_d] and fighter.x < 590:
            fighter.x += 5
        #  2: Draw the fighter
        fighter.draw()
        #  11: Move the enemy_fleet
        #  12: Draw the enemy_fleet
        enemy_fleet.move()
        enemy_fleet.draw()
        #  6: For each missile in the fighter missiles
        #    7: Move the missile
        #    8: Draw the missile
        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        #  12: For each badguy in the enemy_fleet.badguys list
        #      13: For each missile in the fighter missiles
        #          14: If the badguy is hit by the missile
        #              15: Mark the badguy is_dead = True
        #              16: Mark the missile has_exploded = True
        for badguy in enemy_fleet.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.is_dead = True
                    missile.has_exploded = True
                    scoreboard.score += 10
        # 17: Use the fighter to remove exploded missiles
        #  18: Use the enemy_fleet to remove dead badguys
        for missile in fighter.missiles:
            if missile.y > screen.get_height() + 10:
                missile.has_exploded = True
        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()
        #  19: If the enemy is_defeated
        #      20: Increment the enemy_rows
        #      21: Create a new enemy_fleet with the screen and enemy_rows
        if enemy_fleet.is_defeated:
            win_sound.play()
            enemy_rows += 1
            enemy_fleet = EnemyFleet(screen, enemy_rows)
            enemy_fleet.draw()
            enemy_fleet.move()
        #  22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)
        for badguy in enemy_fleet.badguys:
            if badguy.y > 542:
                game_over_sound.play()
                game_over = True




        #  24: Optional extra - Add sound effects!
        scoreboard.draw()
        pygame.display.update()


main()
