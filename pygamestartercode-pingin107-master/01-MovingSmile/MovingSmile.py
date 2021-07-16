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
            if event.type == pygame.KEYDOWN:
                pressedKeys = pygame.key.get_pressed()
                if pressedKeys[pygame.K_UP]:
                    #print("You pressed the Up arrow")
                    eye_y_delta -= 0
                if pressedKeys[pygame.K_DOWN]:
                    #print("You pressed the Down arrow")
                    eye_y_delta += 0
                if pressedKeys[pygame.K_LEFT]:
                    #print("You pressed the Left arrow")
                    eye_x_delta -= 0
                if pressedKeys[pygame.K_RIGHT]:
                    #print("You pressed the Right arrow")
                    eye_x_delta += 0

            # DONE 3: Make the eye pupils move with Up, Down, Left, and Right keys
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_UP]:
            print("You pressed the Up arrow")
            eye_y_delta -= 5
        if pressedKeys[pygame.K_DOWN]:
            print("You pressed the Down arrow")
            eye_y_delta += 5
        if pressedKeys[pygame.K_LEFT]:
            print("You pressed the Left arrow")
            eye_x_delta -= 5
        if pressedKeys[pygame.K_RIGHT]:
            print("You pressed the Right arrow")
            eye_x_delta += 5
        screen.fill((255, 255, 255))  # white

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
        pygame.draw.circle(screen, (0,0,0), (310,245), 7)
        pygame.draw.circle(screen, (0, 0, 0), (330, 245), 7)
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)

        # DONE 2: Draw a mouth
        pygame.draw.rect(screen, (127,0,0), (230,320, 180, 30))
        pygame.draw.circle(screen, (127, 0, 0), (410, 335), 15)
        pygame.draw.circle(screen, (127, 0, 0), (230, 335), 15)
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)

        pygame.display.update()


main()
