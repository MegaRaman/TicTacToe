import pygame
import random
from settings import block_size, margin
from gameGUI.field import Field


class BotField(Field):

    def draw_shape(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        column = x_mouse // (block_size + margin)
        row = y_mouse // (block_size + margin)
        if margin % (block_size + margin) < x_mouse % (block_size + margin) and \
                margin % (block_size + margin) < y_mouse % (block_size + margin) and column < len(self.positions) \
                and row < len(self.positions[0]) and self.positions[row][column] == 0:
            self.positions[row][column] = 'X'
            if not self.check_win('X'):
                self.computer_logic()

    def computer_logic(self):
        # see 2 makes 3
        for row in range(len(self.positions)):
            if self.positions[row].count('O') == 2 and self.positions[row].count('X') == 0:
                self.positions[row][self.positions[row].index(0)] = 'O'
                return

        for column in range(3):
            statements = [self.positions[0][column] == 'O', self.positions[1][column] == 'O',
                          self.positions[2][column] == 'O']
            if statements.count(True) == 2 and self.positions[statements.index(False)][column] == 0:
                self.positions[statements.index(False)][column] = 'O'
                return

        statements = [self.positions[0][0] == 'O', self.positions[1][1] == 'O', self.positions[2][2] == 'O']
        if statements.count(True) == 2 and self.positions[statements.index(False)][statements.index(False)] == 0:
            self.positions[statements.index(False)][statements.index(False)] = 'O'
            return

        statements = [self.positions[0][2] == 'O', self.positions[1][1] == 'O', self.positions[2][0] == 'O']
        if statements.count(True) == 2:
            if statements.index(False) == 0:
                if self.positions[0][2] == 0:
                    self.positions[0][2] = 'O'
                    return
            if statements.index(False) == 1:
                if self.positions[1][1] == 0:
                    self.positions[1][1] = 'O'
                    return
            elif self.positions[2][0] == 0:
                self.positions[2][0] = 'O'
                return

        # stopping from win
        for row in range(len(self.positions)):
            if self.positions[row].count('X') == 2 and self.positions[row].count('O') == 0:
                self.positions[row][self.positions[row].index(0)] = 'O'
                return

        for column in range(3):
            statements = [self.positions[0][column] == 'X', self.positions[1][column] == 'X',
                          self.positions[2][column] == 'X']
            if statements.count(True) == 2 and self.positions[statements.index(False)][column] == 0:
                self.positions[statements.index(False)][column] = 'O'
                return

        statements = [self.positions[0][0] == 'X', self.positions[1][1] == 'X', self.positions[2][2] == 'X']
        if statements.count(True) == 2 and self.positions[statements.index(False)][statements.index(False)] == 0:
            self.positions[statements.index(False)][statements.index(False)] = 'O'
            return

        statements = [self.positions[0][2] == 'X', self.positions[1][1] == 'X', self.positions[2][0] == 'X']
        if statements.count(True) == 2:
            if statements.index(False) == 0:
                if self.positions[0][2] == 0:
                    self.positions[0][2] = 'O'
                    return
            if statements.index(False) == 1:
                if self.positions[1][1] == 0:
                    self.positions[1][1] = 'O'
                    return
            elif self.positions[2][0] == 0:
                self.positions[2][0] = 'O'
                return

        # random turn
        nulls = []
        for row in range(len(self.positions)):
            for column in range(len(self.positions[row])):
                if self.positions[row][column] == 0:
                    nulls.append((row, column))
        random_element = random.choice(nulls)
        self.positions[random_element[0]][random_element[1]] = 'O'
        return
