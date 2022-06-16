import pygame
from gameLogic.functions import paste_picture, set_text
played = {}
texts = []


class Button:
    def __init__(self, width, height, display):
        self.width = width
        self.height = height
        self.display = display

        self.mouse_pos = pygame.mouse.get_pos()

    def draw_button(self, x, y, text, action=None):
        global played, texts
        if text not in texts:
            texts.append(text)
            played[text] = False
        click = pygame.mouse.get_pressed()
        if x < self.mouse_pos[0] < x + self.width and y < self.mouse_pos[1] < y + self.height:
            paste_picture('./pictures/blue_button.png', self.width + 10,
                          self.height, x + self.width // 2 + 5, y + self.height // 2, self.display)
            if click[0]:
                self.play_button_pressed()
                pygame.time.delay(300)
                if action:
                    action()
            if not played[text]:
                self.play_button_hover()
                played[text] = True

        else:
            paste_picture('./pictures/green_button.png', self.width - 15,
                          self.height - 15, x + self.width // 2, y + self.height // 2, self.display)
            played[text] = False
        self.set_text(x + self.width // 2, y + self.height // 2, text)

    @staticmethod
    def play_button_hover():
        sound = pygame.mixer.Sound('./sounds/button_hover.mp3')
        pygame.mixer.Sound.play(sound)

    @staticmethod
    def play_button_pressed():
        sound = pygame.mixer.Sound('./sounds/sword_sound.wav')
        pygame.mixer.Sound.play(sound)

    def set_text(self, x, y, text):
        set_text(x, y, text, self.display)
