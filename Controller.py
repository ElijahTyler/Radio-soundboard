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
animatronic_at_door = pygame.mixer.Sound(os.path.join(maindir, 'assets', 'sounds', 'animatronic_at_door.mp3'))
sfx_channel = pygame.mixer.Channel(1)

def main():
    font_size = 40
    margin = 40
    num_buttons = 9
    volume = 1.0
    sfx_channel.set_volume(volume)
    
    pts = []
    for i in range(num_buttons):
        pts.append((margin, margin + (i)*(font_size + margin)))
    b1 = Button('6AM Chime', font_size, chime_6am, pts[0])
    b2 = Button('Balloon Boy Hello/Hi', font_size, balloon_boy, pts[1])
    b3 = Button('Hallway Ambience', font_size, hallway_ambience, pts[2])
    b4 = Button('Main Menu', font_size, main_menu, pts[3])
    b5 = Button('Mascot Tune', font_size, mascot_tune, pts[4])
    b6 = Button('Music Box', font_size, music_box, pts[5])
    b7 = Button('Power Lost', font_size, power_lost, pts[6])
    b8 = Button('Security Ambience', font_size, security_ambience, pts[7])
    b9 = Button('Animatronic at Door', font_size, animatronic_at_door, pts[8])
    max_width = 0
    for b in [b1, b2, b3, b4, b5, b6, b7, b8]:
        if b.rendered_text_rect.width > max_width:
            max_width = b.rendered_text_rect.width

    screen = Screen(max_width + (2 * margin), (font_size * num_buttons) + ( margin * (num_buttons + 1) ), None, (40,40,40))
    
    screen.add_button(b1)
    screen.add_button(b2)
    screen.add_button(b3)
    screen.add_button(b4)
    screen.add_button(b5)
    screen.add_button(b6)
    screen.add_button(b7)
    screen.add_button(b8)
    screen.add_button(b9)

    last_button = None

    while True:
        if sfx_channel.get_busy():
            pygame.display.set_caption('Radio soundboard - Volume: ' + str(volume) + ' Now playing: ' + last_button.name)
        else:
            pygame.display.set_caption('Radio soundboard - Volume: ' + str(volume))

        screen.draw()

        mouse = pygame.mouse.get_pos()
        for b in screen.buttons:
            if b.rect.collidepoint(mouse):
                b.draw(screen.display, True)
            else:
                b.draw(screen.display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in screen.buttons:
                    if button.rect.collidepoint(event.pos):
                        did_stop = False
                        if sfx_channel.get_busy():
                            sfx_channel.stop()
                            did_stop = True
                        if button != last_button or not did_stop:
                            sfx_channel.play(button.sound)
                            last_button = button
            # else if key pressed is a number 1-9, fade out that many seconds in the sfx_channel
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit() and int(event.unicode) in range(1, 10):
                    sfx_channel.fadeout(int(event.unicode) * 1000)
                elif event.key == pygame.K_0:
                    sfx_channel.fadeout(10000)
                elif event.key == pygame.K_UP and volume < 1.5:
                    volume += 0.05
                    volume = round(volume, 2)
                    sfx_channel.set_volume(volume)
                elif event.key == pygame.K_DOWN and volume > 0.05:
                    volume -= 0.05
                    volume = round(volume, 2)
                    sfx_channel.set_volume(volume)

        pygame.display.update()

if __name__ == "__main__":
    main()