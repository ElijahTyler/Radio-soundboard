from distutils.core import setup
import py2exe

[('assets/sounds', ['assets/sounds/animatronic_at_door.mp3', 'assets/sounds/balloon_boy.mp3', 'assets/sounds/chime_6am.mp3', 'assets/sounds/hallway_ambience.mp3', 'assets/sounds/main_menu.mp3', 'assets/sounds/mascot_tune.mp3', 'assets/sounds/music_box.mp3', 'assets/sounds/power_lost.mp3', 'assets/sounds/security_ambience.mp3'])]

'''
add each sound file to the list of data files
pyinstaller --add-data "assets/sounds/animatronic_at_door.mp3;assets/sounds" --add-data "assets/sounds/balloon_boy.mp3;assets/sounds" --add-data "assets/sounds/chime_6am.mp3;assets/sounds" --add-data "assets/sounds/hallway_ambience.mp3;assets/sounds" --add-data "assets/sounds/main_menu.mp3;assets/sounds" --add-data "assets/sounds/mascot_tune.mp3;assets/sounds" --add-data "assets/sounds/music_box.mp3;assets/sounds" --add-data "assets/sounds/power_lost.mp3;assets/sounds" --add-data "assets/sounds/security_ambience.mp3;assets/sounds" bob_the_bilder.py

'''