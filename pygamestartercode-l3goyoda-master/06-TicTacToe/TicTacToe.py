import pygame
import sys
import os

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
        self.board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        self.game_state_string = "Turn: X"
        self.turn_counter = 0
        self.game_is_over = False

    def __repr__(self):
        return f"Board: {self.board} Turn Counter: {self.turn_counter} State: {self.game_state_string}"

    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        if self.game_is_over:
            return
        if row < 0 or row > 2 or col < 0 or col > 2:
            return
        if self.board[row][col] != ".":
            return
        if self.turn_counter % 2 == 0:
            self.board[row][col] = "X"
            self.game_state_string = "Turn: O"
        else:
            self.board[row][col] = "O"
            self.game_state_string = "Turn: X"
        self.turn_counter += 1
        self.check_for_game_over()

    def check_for_game_over(self):
        # TODO 18: If the turn_counter is 9 then the game is over
        #      If >=9 update the game_is_over value and set the game_state_string to "Tie Game"
        if self.turn_counter >= 9:
            self.game_is_over = True
            self.game_state_string = "Tie - game"
        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

        # TODO 19: Use the lines list to determine if there is a winner.
        #    If there is a winner, update the game_state_string, play a sound, and set game_is_over to True.
        for line in lines:
            if line == "000":
                self.game_is_over = True
                self.game_state_string = "O wins!"
                pygame.mixer.music.play()
            if line == "XXX":
                self.game_is_over = True
                self.game_state_string = "X wins!"
                pygame.mixer.music.play()
            
            


# --------------------------- View Controller ---------------------------

class ViewController:

    def __init__(self, screen):
        self.screen = screen
        self.game = Game()
        self.board_image = pygame.image.load("board.png")
        self.xi = pygame.image.load("x_mark.png")
        self.oi = pygame.image.load("o_mark.png")

    def check_event(self, event):
        # TODO 16: If the event is pygame.MOUSEBUTTONUP
        #     Get the mouse click position as x and y variables
        #     Convert the x and y variables into row and col using get_row_col
        #     Inform the model object about this event
        # TODO 17: If the event is pygame.KEYDOWN
        #     Get the pressed_keys
        #     If the key is pygame.K_SPACE, then reset the game.
        pass

    def draw(self):
        """ Draw the board based on the marked store in the board configuration array """
        # TODO 13: Blit the board_image onto the screen at the x y position of row=0 col=0
        # TODO 14: Use a nested loop (via range) to go over all marks of the game.board
        #    If the mark is "X", blit an X image at the x y position of row col
        #    If the mark is "O", blit an O image at the x y position of row col
        # TODO 15: Update the display caption to be the game.game_state_string
        pass

# --------------------------- Controller ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    view_controller = ViewController(screen)


    print(view_controller.game)
    view_controller.game.take_turn(1, 1)
    print(view_controller.game)
    view_controller.game.take_turn(2, 1)
    print(view_controller.game)
    view_controller.game.take_turn(0, 0)
    print(view_controller.game)
    view_controller.game.take_turn(1, 2)
    print(view_controller.game)
    view_controller.game.take_turn(2, 2)
    print(view_controller.game)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            view_controller.check_event(event)
        screen.fill(pygame.Color("white"))
        view_controller.draw()
        pygame.display.update()


main()
