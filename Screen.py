import pygame
import Button
import os
maindir = os.path.dirname(os.path.abspath(__file__))

class Screen:
    def __init__(self, width, height, bkgd_pic=None, bkgd_color=(0,0,0)):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))
        if bkgd_pic:
            self.bkgdpic = os.path.join(maindir, 'imgs', bkgd_pic)
        else:
            self.bkgdpic = None
        self.bkgd_color = bkgd_color
        self.buttons = []
    
    def draw(self):
        if self.bkgdpic:
            self.display.blit(self.bkgdpic, (0,0))
        else:
            self.display.fill(self.bkgd_color)
    
    def add_button(self, button):
        if button not in self.buttons:
            self.buttons.append(button)
        else:
            print("Button already added")