import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode ((600, 600))
    pygame.display.set_caption("My Own Moving Smile")
    eye_x_delta = 0
    eye_y_delta = 0
    clock = pygame.time.Clock()


    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

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

        # pygame.draw.circle(surface, color, center, radius, width)
        pygame.draw.circle(screen, (255, 255, 0), (300, 300), 200)
        pygame.draw.circle(screen, (0, 0, 0), (300, 300), 200, 3)

        pygame.draw.circle(screen, (255, 255, 255), (225, 250), 25)
        pygame.draw.circle(screen, (0, 0, 0), (225, 250), 25, 3)

        pygame.draw.circle(screen, (255, 255, 255), (375, 250), 25)
        pygame.draw.circle(screen, (0, 0, 0), (375, 250), 25, 3)

        pygame.draw.circle(screen, (0, 0, 0), (225 + eye_x_delta, 250 + eye_y_delta), 5)
        pygame.draw.circle(screen, (0, 0, 0), (375 + eye_x_delta, 250 + eye_y_delta), 5)

        # pygame.draw.rect(surface, color, rect, width, border radius)
        pygame.draw.rect(screen, (0, 0, 0), (215, 350, 180, 30))
        # YOU DON'T HAVE THE RECTANGLE FIGURED OUT YET BUT THAT'S OKAY

        pygame.display.update()

main()