import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    eye_x_delta = 0
    eye_y_delta = 0
    clock = pygame.time.Clock()
    while True:
        # DONE 4: Set the clock speed to 60 fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # DONE 3: Make the eye pupils move with Up, Down, Left, and Right keys
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    print("You pressed the up arrow!")
                    eye_y_delta -= 5
                if pressed_keys[pygame.K_DOWN]:
                    print("You Pressed the down arrow")
                    eye_y_delta += 5
                if pressed_keys[pygame.K_RIGHT]:
                    print("You pressed the right arrow!")
                    eye_x_delta += 5
                if pressed_keys[pygame.K_LEFT]:
                    print("You pressed the left arrow!")
                    eye_x_delta -= 5




            screen.fill((255, 255, 255))  # white
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            print("You pressed the up arrow!")
            eye_y_delta -= 5
        if pressed_keys[pygame.K_DOWN]:
            print("You Pressed the down arrow")
            eye_y_delta += 5
        if pressed_keys[pygame.K_RIGHT]:
            print("You pressed the right arrow!")
            eye_x_delta += 5
        if pressed_keys[pygame.K_LEFT]:
            print("You pressed the left arrow!")
            eye_x_delta -= 5
        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_x_delta, 162 + eye_y_delta), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_x_delta, 162 + eye_y_delta), 7)  # black pupil

        # DONE 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        pygame.draw.circle(screen, (0, 255, 120), (320, 245), 10)
        # Done 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        pygame.draw.rect(screen, (255, 50, 255), (230, 320, 180, 30))
        pygame.display.update()


main()
