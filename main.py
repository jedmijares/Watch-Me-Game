#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import os
import sys

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

# from pyboy import PyBoy, WindowEvent, botsupport # isort:skip
from pyboy import *

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    # print("Usage: python gamewrapper_kirby.py [ROM file]")
    # exit(1)
    filename = r"./ROM/Game & Watch Gallery (USA).gb"

quiet = "--quiet" in sys.argv
# pyboy = PyBoy(filename) # , window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
emu = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet) # , game_wrapper=True)

emu.set_emulation_speed(1)
assert emu.cartridge_title() == "G&W GALLERY"

# for _ in range(480):
#     emu.tick()
# print("press A")
# emu.send_input(WindowEvent.PRESS_BUTTON_A)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_BUTTON_A)

# for _ in range(240):
#     emu.tick()
# print("press left")
# emu.send_input(WindowEvent.PRESS_ARROW_LEFT)
# for _ in range(6):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_ARROW_LEFT)

# for _ in range(60):
#     emu.tick()
# emu.send_input(WindowEvent.PRESS_BUTTON_A)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_BUTTON_A)

# for _ in range(60):
#     emu.tick()
# emu.send_input(WindowEvent.PRESS_BUTTON_A)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_BUTTON_A)

# for _ in range(60):
#     emu.tick()
# emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)

# for _ in range(60):
#     emu.tick()
# emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)

# for _ in range(60):
#     emu.tick()
# emu.send_input(WindowEvent.PRESS_BUTTON_A)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_BUTTON_A)

def getScore():
    score = 0
    score += int(emu.get_memory_value(0xC114))
    score += int(emu.get_memory_value(0xC113)) * 10
    score += int(emu.get_memory_value(0xC112)) * 100
    return score

# while not emu.tick():
#     # print(getScore())
#     pass

# def game_area():
#         """
#         This method returns a cut-out of the screen as a simplified matrix for use in machine learning applications.
#         Returns
#         -------
#         memoryview:
#             Simplified 2-dimensional memoryview of the screen
#         """
#         tiles_matrix = pyboy._game_area_tiles()
#         sprites = pyboy._sprites_on_screen()
#         xx = pyboy.game_area_section[0]
#         yy = pyboy.game_area_section[1]
#         width = pyboy.game_area_section[2]
#         height = pyboy.game_area_section[3]
#         for s in sprites:
#             _x = (s.x // 8) - xx
#             _y = (s.y // 8) - yy
#             if 0 <= _y < height and 0 <= _x < width:
#                 tiles_matrix[_y][_x] = s.tile_identifier
#         return tiles_matrix

# bot = pyboy.botsupport(pyboy, 0)
# print()

while True:
    for _ in range(60):
        emu.tick()
    # print(pyboy.())