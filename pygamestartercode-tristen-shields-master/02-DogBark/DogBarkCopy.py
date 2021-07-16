import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Unfunny Dog Meme")
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    image1 = pygame.image.load("2dogs.JPG")
    font1 = pygame.font.Font(None, 28)
    font2 = pygame.font.Font(None, 50)
    bark_sound = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            if event == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        screen.fill(WHITE)
        image1 = pygame.transform.scale(image1, (600, 500))
        screen.blit(image1, (0, 0))
        caption1 = font1.render("Two Dogs", True, BLACK)
        screen.blit(caption1, (screen.get_width() / 2 - caption1.get_width() / 2, image1.get_height() + 5))
        caption2 = font2.render("WHEN YOU", True, WHITE)
        screen.blit(caption2, (screen.get_width() / 2 - caption2.get_width() / 2, 0))

        pygame.display.update()


main()