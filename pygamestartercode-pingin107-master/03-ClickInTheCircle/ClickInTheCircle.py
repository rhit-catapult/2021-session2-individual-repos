import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]
    deltaX = point1_x - point2_x
    deltaY = point1_y - point2_y
    #  4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    answer = math.sqrt(deltaX ** 2 + deltaY ** 2)
    return answer

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)
    pygame.mixer.music.load("drums.wav")
    #  8: Load the "drums.wav" file into the pygame music mixer
    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #  2: For a MOUSEBUTTONDOWN event get the click position.
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                print(f"x={click_position[0]} y={click_position[1]}")
            #  3: Determine the distance between the click position and the circle_center using the distance
            #  3:   function and save the result into a variable called distance_from_circle
                distance_from_center = distance(click_position, circle_center)
                print(distance_from_center)
            #  5: If distance_from_circle is less than or equal to circle_radius, set message_text to 'Bullseye!'
            #  5: If distance_from_circle is greater than the circle_radius, set the message_text to 'You missed!'
                if distance_from_center < 50:
                    message_text = "You hit inside the circle!"
                    pygame.mixer.music.play(-1)
                    print("win")
                elif 70 > distance_from_center > 50:
                    message_text = "You got so close!"
                    pygame.mixer.music.stop()
                    print("loss")

                else:
                    message_text = "You totally missed!"
                    print("loss")
                    pygame.mixer.music.stop()
            #  9: Start playing the music mixer looping forever if the click is within the circle
            #  10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        #  1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)
        #  6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        font1 = pygame.font.SysFont("Impact", 20)
        textImage = font1.render(message_text, True, text_color)
        screen.blit(textImage, (5, screen.get_height() - 30))
        screen.blit(instructions_image, (25, 25))
        #  7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'

        pygame.display.update()


main()
