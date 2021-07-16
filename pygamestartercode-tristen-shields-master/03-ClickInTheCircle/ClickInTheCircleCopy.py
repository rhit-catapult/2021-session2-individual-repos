import pygame
import sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point1_y = point1[1]
    point2_x = point2[0]
    point2_y = point2[1]

    # Make the distance formula
    return math.sqrt((point2_x + point1_x) ** 2 + (point2_y + point1_y) ** 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Click in the Circle")
    font1 = pygame.font.Font(None, 28)

    drums = pygame.mixer.Sound("drums.wav")

    instruction_text = "Click in the circle"
    text_color = (222, 222, 0)
    instructions_image = font1.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

            if event == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                print(click_position)

                distance_from_center = distance(click_position, circle_center)
                print("Distance from center= ", distance_from_center)

                if distance_from_center <= circle_radius:
                    message_text = "Bullseye!"
                    print(message_text)
                    pygame.mixer.Sound.play(drums)
                else:
                    message_text = "You missed!"
                    print(message_text)
                    pygame.mixer.Sound.stop(drums)

        screen.fill(pygame.Color("Black"))

        pygame.draw.circle(screen, (154, 58, 212), (screen.get_width() // 2, screen.get_height() // 2), 50, 3)
        caption1 = font1.render(message_text, True, (154, 58, 212))

        screen.blit(instructions_image, (25, 25))
        screen.blit(caption1, (10, screen.get_height() - 50))

        pygame.display.update()


main()
