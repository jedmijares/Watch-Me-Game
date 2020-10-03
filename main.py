#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import os
import sys

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

from pyboy import PyBoy, WindowEvent # isort:skip

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    # print("Usage: python gamewrapper_kirby.py [ROM file]")
    # exit(1)
    filename = r"./ROM/Game & Watch Gallery (USA).gb"

quiet = "--quiet" in sys.argv
pyboy = PyBoy(filename) # , window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
# pyboy.set_emulation_speed(0)
assert pyboy.cartridge_title() == "G&W GALLERY"

for _ in range(480):
    pyboy.tick()
print("press A")
pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(240):
    pyboy.tick()
print("press left")
pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
for _ in range(6):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)

for _ in range(60):
    pyboy.tick()
pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(60):
    pyboy.tick()
pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(60):
    pyboy.tick()
pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
for _ in range(12):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)

for _ in range(60):
    pyboy.tick()
pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
for _ in range(12):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)

for _ in range(60):
    pyboy.tick()
pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
# for _ in range(60):
#     pyboy.tick()

while not pyboy.tick():
    pass

# gaw = pyboy.game_wrapper()
# gaw.start_game()

# assert kirby.score == 0
# assert kirby.lives_left == 4
# assert kirby.health == 6

# pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)

# for _ in range(280): # Walk for 280 ticks
#     pyboy.tick()

# assert kirby.score == 800
# assert kirby.health == 5

# print(kirby)

# kirby.reset_game()
# assert kirby.score == 0
# assert kirby.health == 6

# pyboy.stop()
