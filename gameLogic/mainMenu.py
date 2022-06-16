import pygame
from gameGUI.button import Button
from settings import fps, width
from gameLogic.userAgainstUser import AgainstFriend
from gameLogic.userAgainstComputer import AgainstComputer


class Menu:
    """Class that describes the main menu of a program"""
    bg = pygame.image.load('./pictures/background_main_menu.jpg')

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

        self.menu = True
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.blit(self.bg, (0, 0))
            self.buttons()
            pygame.display.update()
            self.clock.tick(fps)

    def buttons(self):
        vs_friend_button = Button(200, 60, self.screen)
        vs_friend_button.draw_button(width // 2 - 110, 150, "Play with friend", action=self.versus_human_button)
        vs_computer_button = Button(200, 60, self.screen)
        vs_computer_button.draw_button(width // 2 - 110, 210, "Play with computer", action=self.versus_computer_button)
        exit_button = Button(200, 60, self.screen)
        exit_button.draw_button(width // 2 - 110, 270, "Exit", action=self.exit)

    def versus_human_button(self):
        AgainstFriend(self.screen, self.clock)

    def versus_computer_button(self):
        AgainstComputer(self.screen, self.clock)

    @staticmethod
    def exit():
        pygame.time.delay(500)
        pygame.quit()
        quit()

