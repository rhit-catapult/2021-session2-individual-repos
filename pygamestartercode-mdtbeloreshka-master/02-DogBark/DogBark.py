import pygame
import sys
# can also be written as import pygame, sys

def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30
    # these variables are constants so they are put in uppercase
    # defining the constants at the beginning to make our lives easier

    # initialize the pygame module
    pygame.init()

    # Load the music and the image
    # TODO 1: Create an image with the 2dogs.JPG image
    image1 = pygame.image.load("2dogs.JPG")
    # the right way to learn is to look at tutorials and/or make reasonable guesses

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
    pygame.display.set_caption("Text, Sound, and an Image")

    # TODO 4: Create a font object with a size 28 font.
    # caption #1 at the bottom
    font1 = pygame.font.Font(None, 28)
    # caption #2 at the top
    font2 = pygame.font.Font(None, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        screen.blit(image1, (0, 0))
        # the image is 739 X 739 so it's zoomed in --> we need to scale it before we blit it
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)

        # create the bottom caption "Two Dogs"
        caption1= font1.render("Two Dogs", True, BLACK)
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption1, (IMAGE_SIZE / 2 - caption1.get_width() / 2, 477))
        # screen.blit(caption1, (IMAGE_SIZE // 2 - caption1.get_width() // 2, 477)) makes it so that the numbers are integers
        # which is useful since math with integers is easier on the computer, popular
        # so that the caption is in the middle of the screen

        # create the top caption "NO FAIR!"
        caption2 = font2.render("NO FAIR!", True, WHITE)
        screen.blit(caption2, (IMAGE_SIZE / 2 - caption2.get_width() / 2, 20))
        # crtl+C & crtl+V all day every day
        # Update the screen
        pygame.display.update()

    # create/add the sound
    # mp3 and wav are different
    bark_sound = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.ext()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

    # OR another sound option, more so used for background music
    # pygame.mixer.music.load("bark.mp3")
    # while True:
    #   for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #           sys.ext()
    #        if event.type == pygame.MOUSEBUTTONDOWN:
    #           pygame.mixer.music.play(-1)
    #        if event.type == pygame.MOUSEBUTTONUP:
    #           pygame.mixer.music.stop()

main()
