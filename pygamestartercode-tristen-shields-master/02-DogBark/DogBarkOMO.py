import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("My Own Dog Meme")
    image1 = pygame.image.load("2dogs.JPG")
    font1 = pygame.font.Font(None, 28)
    font2 = pygame.font.Font(None, 100)
    bark_sound = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            if event == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        screen.fill((255, 255, 255))
        screen.blit(image1, (0, 0))

        bottom_caption = font1.render("Two Dogs", True, (0, 0, 0))
        screen.blit(bottom_caption, (screen.get_width() / 2 - bottom_caption.get_width() / 2, image1.get_height()))

        top_caption = font2.render("WHEN YOU", True, (255, 255, 255))
        screen.blit(top_caption, (screen.get_width() / 2 - top_caption.get_width() / 2, 0))

        pygame.display.update()


main()