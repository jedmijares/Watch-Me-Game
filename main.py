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
emu = PyBoy(filename) # , window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
# emu = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet) # , game_wrapper=True)

emu.set_emulation_speed(1)
assert emu.cartridge_title() == "G&W GALLERY" # do not proceed if the is not Game & Watch Gallery

for _ in range(480):
    emu.tick()
print("press A")
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(240):
    emu.tick()
print("press left")
emu.send_input(WindowEvent.PRESS_ARROW_LEFT)
for _ in range(6):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_ARROW_LEFT)

for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)

# for _ in range(60):
#     emu.tick()
# emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
# for _ in range(12):
#     emu.tick()
# emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)

for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)

def getScore():
    score = 0
    score += int(emu.get_memory_value(0xC114))
    score += int(emu.get_memory_value(0xC113)) * 10
    score += int(emu.get_memory_value(0xC112)) * 100
    return score

# while not emu.tick():
#     # print(getScore())
#     pass

def getNPClocations(spriteList):
    NPClocations = []
    for sublist in spriteList:
        for spriteIndex in sublist:
            NPCsprite = emu.botsupport_manager().sprite(spriteIndex)
            NPClocations.append((NPCsprite.x, NPCsprite.y))
    return NPClocations

manSpriteIndices = emu.botsupport_manager().sprite_by_tile_identifier(list(range(16,24,2)))
NPClocations = (getNPClocations(manSpriteIndices))
lastNPClocations = NPClocations.copy()
while True:
    # emu.tick()
    # sprite identifer for the NPC characters range from 16 - 23 and 32 - 39
    # 32 - 39 is the "bottom half" of 16 - 23, so we don't need it for finding their locations
    # we can iterate by 2 because the NPC is 2 sprites wide
    manSpriteIndices = emu.botsupport_manager().sprite_by_tile_identifier(list(range(16,24,2)))
    lastNPClocations = NPClocations
    NPClocations = (getNPClocations(manSpriteIndices))
    if NPClocations != lastNPClocations:
        if(NPClocations):
            print(NPClocations)
    
    if (32, 25) in NPClocations:
        emu.send_input(WindowEvent.PRESS_ARROW_LEFT)
        emu.tick()
        emu.send_input(WindowEvent.PRESS_ARROW_UP)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_UP)
    elif (80, 25) in NPClocations:
        emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        emu.tick()
        emu.send_input(WindowEvent.PRESS_ARROW_UP)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_UP)
    elif (72, 89) in NPClocations:
        emu.send_input(WindowEvent.PRESS_ARROW_LEFT)
        emu.tick()
        emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    elif (120, 89) in NPClocations:
        emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        emu.tick()
        emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        emu.tick()
        emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    emu.tick()
    
    