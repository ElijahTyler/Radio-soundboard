import pygame
import os
maindir = os.path.dirname(os.path.abspath(__file__))

class Button:
    def __init__(self, name='Untitled', font_size=30, sound=None, pos=(0,0)):
        self.name = name
        self.font = pygame.font.Font(os.path.join(maindir, 'assets', 'Consolas.ttf'), font_size)
        self.sound = sound
        self.pos = pos
        self.rendered_text = self.font.render(self.name, True, (40, 40, 40))
        self.rendered_text_rect = self.rendered_text.get_rect()
        self.rect = pygame.Rect(pos[0], pos[1], self.rendered_text_rect.width, self.rendered_text_rect.height)

    def draw(self, surface, hovering=False):
        c=255-55*hovering
        pygame.draw.rect(surface, (c, c, c), self.rect, 1)
        surface.fill((c, c, c), self.rect)
        surface.blit(self.rendered_text, self.pos)