import pygame
import os
maindir = os.path.dirname(os.path.abspath(__file__))

class Button:
    def __init__(self, name='Untitled', font_size=30, sound=None, pos=(0,0)):
        self.name = name
        self.font = pygame.font.Font(os.path.join(maindir, 'assets', 'font', 'Consolas.ttf'), font_size)
        self.sound = sound
        self.pos = pos
        self.rendered_text = self.font.render(self.name, True, (255, 255, 255))
        self.rendered_text_rect = self.rendered_text.get_rect()
        self.rect = pygame.Rect(pos[0], pos[1], self.rendered_text_rect.width, self.rendered_text_rect.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)
        surface.blit(self.rendered_text, self.pos)