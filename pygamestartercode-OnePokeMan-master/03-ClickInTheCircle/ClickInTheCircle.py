import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    pygame.mixer.music.load("drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = pygame.Color("Cyan")
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                distance_from_circle = distance(click_position, circle_center)
                print(distance_from_circle)
                if distance_from_circle <= circle_radius:
                    message_text = "Bullseye!"
                else:
                    message_text = "You missed!"

                if message_text == "Bullseye!":
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()

        screen.fill(pygame.Color("Black"))

        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        font = pygame.font.SysFont('Latin Wide', 50)
        caption = font.render(message_text, True, (122, 237, 201))

        screen.blit(instructions_image, (25, 25))

        screen.blit(caption, (screen.get_width() / 2 - caption.get_width() / 2, 70))

        pygame.display.update()


main()
