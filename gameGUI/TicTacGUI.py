import pygame
from gameLogic.mainMenu import Menu
from settings import width, height


class TicTacGUI:
    """Main class that connects all elements of the game and initializes main cycle"""

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tic-tac-toe Game")
        pygame.display.set_icon(pygame.image.load("./pictures/icon.png"))
        self.clock = pygame.time.Clock()
        self.menu()

    def menu(self):
        Menu(self.screen, self.clock)
