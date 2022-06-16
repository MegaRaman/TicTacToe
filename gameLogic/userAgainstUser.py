import pygame
from settings import fps, white
from gameGUI.field import Field
from gameGUI.button import Button
from gameGUI.messageBox import MessageBox
from gameLogic.functions import set_text


class AgainstFriend:
    bg = pygame.image.load('./pictures/background_main_menu.jpg')
    game_with_friend = True

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

        self.scores = [0, 0]
        self.game_field = Field(self.screen, self)

        self.main_cycle()

    def main_cycle(self):
        self.game_field.clean_field()
        while self.game_with_friend:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.blit(self.bg, (0, 0))
            self.buttons()
            self.scores_table()
            self.game_field.draw_field()
            pygame.display.update()
            self.clock.tick(fps)

    def buttons(self):
        menu_button = Button(200, 60, self.screen)
        menu_button.draw_button(600, 150, "Exit to the menu", action=self.to_menu)

    def to_menu(self):
        self.game_with_friend = False
        self.game_field.clean_field()
        pygame.time.delay(100)

    def message_box(self, x, y, message):
        MessageBox(self.screen, x, y, message, self, self.game_field, self.clock)

    def scores_table(self):
        pygame.draw.rect(self.screen, white, (600, 250, 200, 60), 0, 5)
        set_text(700, 280, 'SCORES', self.screen, font_size=30)
        pygame.draw.rect(self.screen, white, (600, 313, 98, 60), 0, 5)
        set_text(649, 343, 'X', self.screen, font_size=45)
        pygame.draw.rect(self.screen, white, (702, 313, 98, 60), 0, 5)
        set_text(751, 343, 'O', self.screen, font_size=45)
        pygame.draw.rect(self.screen, white, (600, 376, 98, 60), 0, 5)
        set_text(649, 406, str(self.scores[0]), self.screen, font_size=45,
                 font_type='./font/JosefinSans-Italic-VariableFont_wght.ttf')
        pygame.draw.rect(self.screen, white, (702, 376, 98, 60), 0, 5)
        set_text(751, 406, str(self.scores[1]), self.screen, font_size=45,
                 font_type='./font/JosefinSans-Italic-VariableFont_wght.ttf')
