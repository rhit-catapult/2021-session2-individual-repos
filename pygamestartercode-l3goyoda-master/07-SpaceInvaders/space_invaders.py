import pygame, sys


class Missile:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = 591
        self.has_exploded = False

    def move(self):
       self.y -= 25

    def draw(self):
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.missiles = []
        self.x = x
        self.y = y
        self.image = pygame.image.load("fighter.png")
        self.pew = pygame.mixer.Sound("pew.wav")
        pygame.Surface.set_colorkey(self.image, (255, 255, 255))


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        new_missile = Missile(self.screen, self.x + 75)
        self.missiles.append(new_missile)
        new_missile = Missile(self.screen, self.x + 25)
        self.missiles.append(new_missile)
        self.pew.play()

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
        self.image = pygame.image.load("badguy.png")
        self.is_dead = False
        self.original_x = x
        self.move_right = True

    def move(self):
        if abs(self.x - self.original_x) > 100:
            self.speed = self.speed * -1
            self.y += abs(self.speed) * 4  
            self.x += self.speed  
        else:
            self.x += self.speed
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(missile.x, missile.y)
class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))
        self.death = pygame.mixer.Sound("explosion.wav")
        self.win = pygame.mixer.Sound("win.wav")
    def is_defeated(self):
        if len(self.badguys) == 0:
            return True
        else: 
            return False

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
                self.death.play()

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont(None, 28)
    def draw(self):
        caption = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(caption, (10, 10))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))
    enemy_rows = 1
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    fighter = Fighter(screen, 320, 590)
    game_over = False
    overimage = pygame.image.load("gameover.png")
    scoreboard = Scoreboard(screen)
    score = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_s] or pressed_keys[pygame.K_d] or pressed_keys[pygame.K_f]:
                    fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            fighter.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            fighter.x += 10
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
                    scoreboard.score += 10

        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()

        if enemy_fleet.is_defeated():
            enemy_rows += 1
            enemy_fleet = EnemyFleet(screen, enemy_rows)
            enemy_fleet.win.play()

        for badguy in enemy_fleet.badguys:
            if badguy.y > 545:
                game_over = True
                screen.blit(overimage, (170, 200))


        scoreboard.draw()
        pygame.display.update()


main()
