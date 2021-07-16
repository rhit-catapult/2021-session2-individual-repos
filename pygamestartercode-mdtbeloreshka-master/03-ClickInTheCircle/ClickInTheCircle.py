import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)
    # distance function


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")

    # TODO 8: Load the "drums.wav" file into the pygame music mixer

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    drum_sound = pygame.mixer.Sound("drums.wav")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO 2: For a MOUSEBUTTONDOWN event get the click position.
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                print("Click Position: ", click_position)
                print(f"x={click_position[0]}, y={click_position[1]}")  # this is a tuple

                distance_from_center = distance(click_position, circle_center)
                print("Distance from the center =", distance_from_center)

                # message if you hit the circle or not
                if distance_from_center > circle_radius:
                    message_text = "You missed!"
                    drum_sound.stop()  # stop playing the music if the click is outside the circle
                if distance_from_center <= circle_radius:
                    message_text = "Bullseye!"
                    drum_sound.play(-1)   # start playing the music mixer looping forever if the click is
                    # within the circle

                # OR
                # if distance_from_center <= circle_radius
                #   message_text = "Bullseye!"
                # else:
                #   message_text = "You missed!"

        screen.fill(pygame.Color("Black"))

        # TODO 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)
        # TODO 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        font1 = pygame.font.Font(None, 28)
        caption1 = font1.render("message_text", True, WHITE)

        screen.blit(instructions_image, (25, 25))
        # TODO 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'
        screen.blit(caption1, (10, screen.get_height() - 30))

        pygame.display.update()

main()
