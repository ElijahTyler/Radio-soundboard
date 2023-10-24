from Screen import Screen
from Button import Button
import pygame
import os
pygame.init()
maindir = os.path.dirname(os.path.abspath(__file__))

chime_6am = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', '6am_chime.mp3'))
balloon_boy = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'balloon_boy.mp3'))
freddy_jumpscare = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'freddy_jumpscare.mp3'))
hallway_ambience = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'hallway_ambience.mp3'))
main_menu = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'main_menu.mp3'))
mascot_tune = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'mascot_tune.mp3'))
sfx_channel = pygame.mixer.Channel(1)

def main():
    screen = Screen(800, 600, None, (40,40,40))
    b1 = Button(100, 50, '6AM Chime', 30, chime_6am, (100, 100))
    b2 = Button(100, 50, 'Balloon Boy Hello/Hi', 30, balloon_boy, (100, 200))
    b3 = Button(100, 50, 'Freddy Jumpscare', 30, freddy_jumpscare, (100, 300))
    b4 = Button(100, 50, 'Hallway Ambience', 30, hallway_ambience, (500, 100))
    b5 = Button(100, 50, 'Main Menu', 30, main_menu, (500, 200))
    b6 = Button(100, 50, 'Mascot Tune', 30, mascot_tune, (500, 300))
    screen.add_button(b1)
    screen.add_button(b2)
    screen.add_button(b3)
    screen.add_button(b4)
    screen.add_button(b5)
    screen.add_button(b6)

    last_button = None

    while True:
        screen.draw()
        for b in screen.buttons:
            b.draw(screen.display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in screen.buttons:
                    if button.rect.collidepoint(event.pos):
                        sfx_channel.stop()
                        if button != last_button or not sfx_channel.get_busy():
                            sfx_channel.play(button.sound)
                            last_button = button

        pygame.display.update()


if __name__ == "__main__":
    main()