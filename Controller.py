from Screen import Screen
from Button import Button
import pygame
import os
pygame.init()
maindir = os.path.dirname(os.path.abspath(__file__))

balloon_boy = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'balloon_boy.mp3'))
chime_6am = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'chime_6am.mp3'))
hallway_ambience = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'hallway_ambience.mp3'))
main_menu = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'main_menu.mp3'))
mascot_tune = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'mascot_tune.mp3'))
music_box = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'music_box.mp3'))
power_lost = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'power_lost.mp3'))
security_ambience = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'security_ambience.mp3'))
sfx_channel = pygame.mixer.Channel(1)

def main():
    font_size = 40
    screen = Screen(600, 800, None, (40,40,40))
    pygame.display.set_caption('Radio soundboard')
    b1 = Button('6AM Chime', font_size, chime_6am, (50, 50))
    b2 = Button('Balloon Boy Hello/Hi', font_size, balloon_boy, (50, 130))
    b3 = Button('Hallway Ambience', font_size, hallway_ambience, (50, 210))
    b4 = Button('Main Menu', font_size, main_menu, (50, 290))
    b5 = Button('Mascot Tune', font_size, mascot_tune, (50, 370))
    b6 = Button('Music Box', font_size, music_box, (50, 450))
    b7 = Button('Power Lost', font_size, power_lost, (50, 530))
    b8 = Button('Security Ambience', font_size, security_ambience, (50, 610))
    screen.add_button(b1)
    screen.add_button(b2)
    screen.add_button(b3)
    screen.add_button(b4)
    screen.add_button(b5)
    screen.add_button(b6)
    screen.add_button(b7)
    screen.add_button(b8)

    last_button = None

    while True:
        screen.draw()
        for b in screen.buttons:
            b.draw(screen.display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in screen.buttons:
                    if button.rect.collidepoint(event.pos):
                        sfx_channel.stop()
                        if button != last_button and not sfx_channel.get_busy():
                            sfx_channel.play(button.sound)
                            last_button = button

        pygame.display.update()


if __name__ == "__main__":
    main()