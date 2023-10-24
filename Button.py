import pygame
import os
maindir = os.path.dirname(os.path.abspath(__file__))

class Button:
    def __init__(self, width, height, name='Untitled', font_size=30, sound=None, pos=(0,0)):
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.name = name
        self.font = pygame.font.Font(os.path.join(maindir, 'assets', 'font', 'Consolas.ttf'), font_size)
        self.rendered_text = self.font.render(name, True, (255, 255, 255))
        self.rendered_text_rect = self.rendered_text.get_rect(center=self.rect.center)
        self.sound = sound

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        surface.blit(self.rendered_text, self.rendered_text_rect)