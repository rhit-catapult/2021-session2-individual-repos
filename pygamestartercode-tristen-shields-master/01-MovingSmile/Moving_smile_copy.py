import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile Copy")
    screen = pygame.display.set_mode((640, 480))
    eye_x_delta = 0
    eye_y_delta = 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    eye_y_delta += -10
                if pressed_keys[pygame.K_DOWN]:
                    eye_y_delta += 10
                if pressed_keys[pygame.K_RIGHT]:
                    eye_x_delta += 10
                if pressed_keys[pygame.K_LEFT]:
                    eye_x_delta += -10

        screen.fill((255, 255, 255))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            eye_y_delta += -10
        if pressed_keys[pygame.K_DOWN]:
            eye_y_delta += 10
        if pressed_keys[pygame.K_RIGHT]:
            eye_x_delta += 10
        if pressed_keys[pygame.K_LEFT]:
            eye_x_delta += -10

        # SURFACE, COLOR, CENTER, RADIUS, WIDTH
        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)

        pygame.draw.circle(screen, (255, 255, 255), (240, 160), 25)
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 4)
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_x_delta, 162 + eye_y_delta), 7)

        pygame.draw.circle(screen, (255, 255, 255), (400, 160), 25)
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 4)
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_x_delta, 162 + eye_y_delta), 7)

        pygame.draw.circle(screen, (0, 0, 0), (320, 245), 10)
        pygame.draw.rect(screen, (0, 0, 0), (230, 320, 180, 30))

        pygame.display.update()

main()