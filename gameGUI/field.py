import pygame
from settings import block_size, margin, white, width, height
from gameLogic.functions import paste_picture


class Field:
    """ Class that describes the game field that consists of three x three white blocks with black margins """
    positions = [[0 for _ in range(3)] for _ in range(3)]
    turn = 0
    flag = False

    def __init__(self, display, parent):
        self.display = display
        self.parent = parent

    def draw_field(self):
        for row in range(len(self.positions)):
            for column in range(len(self.positions[row])):

                x = column * block_size + (column + 1) * margin
                y = row * block_size + (row + 1) * margin

                if self.positions[row][column] == 0:
                    pygame.draw.rect(self.display, white, (x, y, block_size, block_size), 0, 5)

                elif self.positions[row][column] == 'X':
                    paste_picture('./pictures/cross.png', block_size, block_size, x + block_size // 2,
                                  y + block_size // 2, self.display)

                elif self.positions[row][column] == 'O':
                    paste_picture('./pictures/circle_variant1.png', block_size, block_size, x + block_size // 2,
                                  y + block_size // 2, self.display)

        if self.flag:
            if self.check_win('X') == 'X':
                self.parent.message_box(width // 2, height // 2, 'X won\nEnter to restart\nEsc to back to the menu')
            elif self.check_win('X') == 'Draw':
                self.parent.message_box(width // 2, height // 2, 'Draw\nEnter to restart\nEsc to back to the menu')
            if self.check_win('O') == 'O':
                self.parent.message_box(width // 2, height // 2, 'O won\nEnter to restart\nEsc to back to the menu')
            elif self.check_win('O') == 'Draw':
                self.parent.message_box(width // 2, height // 2, 'Draw\nEnter to restart\nEsc to back to the menu')

        if self.check_win('X') == 'X':
            self.flag = True
            self.parent.scores[0] += 1
        elif self.check_win('O') == 'O':
            self.flag = True
            self.parent.scores[1] += 1
        elif self.check_win('O') == 'Draw' or self.check_win('X') == 'Draw':
            self.flag = True

        click = pygame.mouse.get_pressed()[0]
        if click:
            self.draw_shape()

    def draw_shape(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        column = x_mouse // (block_size + margin)
        row = y_mouse // (block_size + margin)
        if margin % (block_size + margin) < x_mouse % (block_size + margin) and \
                margin % (block_size + margin) < y_mouse % (block_size + margin) and column < len(self.positions) \
                and row < len(self.positions[0]) and self.positions[row][column] == 0:
            if self.turn % 2 == 0:
                self.positions[row][column] = 'X'
            else:
                self.positions[row][column] = 'O'
            self.turn += 1

    def check_win(self, shape):
        empty_fields = 0
        for row in self.positions:
            empty_fields += row.count(0)
            if row.count(shape) == 3:
                return shape
        for column in range(3):
            if self.positions[0][column] == shape and self.positions[1][column] == shape and \
                    self.positions[2][column] == shape:
                return shape
        if self.positions[0][0] == shape and self.positions[1][1] == shape and self.positions[2][2] == shape:
            return shape
        if self.positions[0][2] == shape and self.positions[1][1] == shape and self.positions[2][0] == shape:
            return shape
        if empty_fields == 0:
            return 'Draw'
        return False

    def clean_field(self):
        self.positions = [[0 for _ in range(3)] for _ in range(3)]
        self.turn = 0
        self.flag = False


