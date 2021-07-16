import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    eyexdelta = 0
    eyeydelta = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        # TODO 4: Set the clock speed to 60 fps
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressedkeys = pygame.key.get_pressed()
                if pressedkeys[pygame.K_w]:
                    eyeydelta -=1
                if pressedkeys[pygame.K_a]:
                    eyexdelta-=1

                if pressedkeys[pygame.K_s]:
                    eyeydelta+=1
                if pressedkeys[pygame.K_d]:
                    eyexdelta+=1
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_w]:
            eyeydelta -= 5
        if pressedkeys[pygame.K_a]:
            eyexdelta -= 5

        if pressedkeys[pygame.K_s]:
            eyeydelta += 5
        if pressedkeys[pygame.K_d]:
            eyexdelta += 5


        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eyexdelta, 162 + eyeydelta), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eyexdelta, 162 + eyeydelta), 7)  # black pupil

        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        pygame.draw.circle(screen, (80,0,0), (320,245), 10)
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        pygame.draw.rect(screen, (0,0,0), (230,320, 180, 30))
        pygame.display.update()


main()
