import pygame
import sys


# --------------------------- Conversion helper functions ---------------------------


def get_row_col(mouse_x, mouse_y):
    """ Converts an x, y screen position into a row, col value. """
    # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


# --------------------------- Model Object ---------------------------


class Game:
    def __init__(self):
        self.board = [[".",".","."],[".",".","."],[".",".","."]]
        self.gamestatestring = "X's Turn"
        self.turncounter = 0
        self.gameisover = False

    def __repr__(self):
        """ Returns a string that represents the game. """
        return f"Board: {self.board}  Turn Counter: {self.turncounter}  State String: {self.gamestatestring}"
    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        if self.gameisover:
            return
        if row < 0 or row > 2 or col < 0 or col > 2:
            return
        if self.board[row][col] != ".":
            return
        if self.turncounter % 2 == 0:
            self.board[row][col] = "X"
            self.gamestatestring = "O's Turn"
        else:
            self.board[row][col] = "O"
            self.gamestatestring = "X's Turn"

        self.turncounter += 1

        self.check_for_game_over()

    def check_for_game_over(self):
        if self.turncounter == 9:
            self.gameisover = True
            self.gamestatestring = "Tie Game"

        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

        for line in lines:
            if line == "OOO":
                self.gameisover = True
                self.gamestatestring = "O Wins"
                pygame.mixer.music.play()
            if line == "XXX":
                self.gameisover = True
                self.gamestatestring = "X Wins"
                pygame.mixer.music.play()
# --------------------------- View Controller ---------------------------

class ViewController:

    def __init__(self, screen):
        """ Creates the view controller (the Tic-Tac-Toe game you see) """
        self.screen = screen
        self.game = Game()
        self.boardimage = pygame.image.load("board.png")
        self.ximage = pygame.image.load("x_mark.png")
        self.oimage = pygame.image.load("o_mark.png")

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            row, col = get_row_col(event.pos[0], event.pos[1])
            self.game.take_turn(row,col)
        if event.type == pygame.KEYDOWN:
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[pygame.K_SPACE]:
                self.game = Game()

    def draw(self):
        self.screen.blit(self.boardimage, get_xy_position(0,0))
        for row in range(3):
            for col in range(3):
                mark = self.game.board[row][col]
                if mark == "X":
                    self.screen.blit(self.ximage, get_xy_position(row, col))
                if mark == "O":
                    self.screen.blit(self.oimage, get_xy_position(row, col))
        pygame.display.set_caption(self.game.gamestatestring)
# --------------------------- Controller ---------------------------

        pass
def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    viewcontroller = ViewController(screen)
   # print(viewcontroller.game)
    #viewcontroller.game.take_turn(1, 1)
#    viewcontroller.game.take_turn(1, 2)
 #   viewcontroller.game.take_turn(0, 1)
  #  viewcontroller.game.take_turn(1, 0)
   # viewcontroller.game.take_turn(2, 1)
    #viewcontroller.game.take_turn(0, 2)
    #print(viewcontroller.game)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            viewcontroller.check_event(event)

        screen.fill(pygame.Color("white"))
        viewcontroller.draw()
        pygame.display.update()


main()
