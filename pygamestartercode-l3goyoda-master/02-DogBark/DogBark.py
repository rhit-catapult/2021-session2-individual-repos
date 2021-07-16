import pygame
import sys

def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Load the music and the image
    #  1: Create an image with the 2dogs.JPG image
    image1 = pygame.image.load("2dogs.JPG")
    #  4: Create a font object with a size 28 font.
    font1 = pygame.font.Font(None, 28)
    font2 = pygame.font.Font(None, 200)
    #  8: Create a Sound object from the "bark.wav" file.
    sound1 = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONUP:
                sound1.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)
        # Draw the image onto the screen
        #  3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
        #  2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image1, (0,0))
        # Draw the text onto the screen
        #  5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
        caption1 = font1.render("Two Dogs", True, BLACK)
        caption2 = font2.render("E", True, WHITE)
        #  6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption1, (IMAGE_SIZE / 2 - caption1.get_width() / 2, 477))
        screen.blit(caption2, (IMAGE_SIZE / 2 - caption2.get_width() / 2, 25))
        #  7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
