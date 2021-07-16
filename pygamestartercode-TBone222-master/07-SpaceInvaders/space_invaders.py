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
        pygame.draw.line(self.screen, (0,0,255), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.missiles = []
        self.playershipimg = pygame.image.load("fighter.png")
        self.playershipimg.set_colorkey((255,255,255))
        self.fightersound = pygame.mixer.Sound("pew.wav")

    def draw(self):
        self.screen.blit(self.playershipimg, (self.x, self.y))

    def fire(self):
        newmissile = Missile(self.screen, self.x + 50)
        self.missiles.append(newmissile)
        self.fightersound.play()

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("badguy.png")
        self.is_dead = False
        self.originalx = x
        self.moveright = True

    def move(self):
       # if self.moveright == True:
        #    self.x += self.speed
       # if self.moveright == False:
      #      self.x -= self.speed
        self.x += self.speed
        if self.x >= self.originalx + 100 or self.x <= self.originalx - 100:
            self.speed = -self.speed
            self.y += 24

    def draw(self):
        self.screen.blit(self.image, (self.x,self.y))

    def hit_by(self, missile):
        hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(missile.x, missile.y)

class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))
        self.explode = pygame.mixer.Sound("explosion.wav")
    @property
    def is_defeated(self):
        return len(self.badguys) == 0

    def move(self):
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        for badguy in self.badguys:
            badguy.draw()
    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]
                self.explode.play()

class Scoreboard():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font  = pygame.font.SysFont(None, 28)
    def draw(self):
        captionsore = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(captionsore, (10,10))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))
    winsound= pygame.mixer.Sound("win.wav")
    losesound = pygame.mixer.Sound("lose.wav")
    gameover = False
    enemy_rows = 3
    enemyfleet = EnemyFleet(screen, enemy_rows)

    fighter = Fighter(screen, 320, 590)
    scoreboard = Scoreboard(screen)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_p] or  pressed_keys[pygame.K_l]:
                    fighter.fire()

        screen.fill((0, 0, 0))
        if gameover:
            gameoverimg = pygame.image.load("gameover.png")
            screen.blit(gameoverimg, (170, 200))
            pygame.display.update()

            continue
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] and fighter.x >= -50:
            fighter.x -= 5
        if pressed_keys[pygame.K_d] and fighter.x <=590:
            fighter.x += 5

        fighter.draw()

        enemyfleet.move()
        enemyfleet.draw()

        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        for badguy in enemyfleet.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.is_dead = True
                    scoreboard.score += 100
                    missile.has_exploded = True

        for missile in fighter.missiles:
            if missile.y > screen.get_height() + 8:
                missile.has_exploded = True

        fighter.remove_exploded_missiles()

        enemyfleet.remove_dead_badguys()
        if enemyfleet.is_defeated:
            enemy_rows += 1
            winsound.play()
            enemyfleet = EnemyFleet(screen, enemy_rows)

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score
        for badguy in  enemyfleet.badguys:
            if badguy.y >= 545:
                losesound.play()
                gameover = True

        scoreboard.draw()
        pygame.display.update()


main()
