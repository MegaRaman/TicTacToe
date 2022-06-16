import pygame
from settings import red, fps, black, width, height
from gameLogic.functions import set_text, multiLineSurface


class MessageBox:
    def __init__(self, display, x, y, text, parent, field, clock):
        self.x = x
        self.y = y
        self.display = display
        self.text = text
        self.parent = parent
        self.game_field = field
        self.clock = clock

        self.main_cycle()

    def main_cycle(self):
        cont = True
        while cont:
            test = pygame.rect.Rect(200, 200, 500, 300)
            self.display.blit(multiLineSurface(self.text, pygame.font.Font('./font/Brown Holmes DEMO.otf', 20),
                                                        test, black, red), (200, 100))
            pygame.display.update()
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                cont = False
                self.game_field.clean_field()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                cont = False
                self.parent.game_with_friend = False
