# Gerard (Jed) Mijares
# Python script to automatically play Fire

import os
import sys

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

from pyboy import *

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = r"./ROM/Game & Watch Gallery (USA).gb"

quiet = "--quiet" in sys.argv
emu = PyBoy(filename) # , window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
# emu = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet) # , game_wrapper=True)

emu.set_emulation_speed(0)
assert emu.cartridge_title() == "G&W GALLERY" # do not proceed if this is not Game & Watch Gallery

# get player's score
def getScore():
    score = 0
    score += (emu.get_memory_value(0xC114))
    score += (emu.get_memory_value(0xC113)) * 10
    score += (emu.get_memory_value(0xC112)) * 100
    score += (emu.get_memory_value(0xC111)) * 1000
    return score

# get number of lives player has lost
def getMissCount():
    return emu.get_memory_value(0xC115)

# given a list of sprite indices, locate the position of all active NPC characters that need to be saved
def getNPClocations(spriteList):
    NPClocations = []
    for sublist in spriteList:
        for spriteIndex in sublist:
            NPCsprite = emu.botsupport_manager().sprite(spriteIndex)
            if NPCsprite.x in {32, 80, 72, 120}: # these are the only x positions that NPCs about to fall appear
                NPClocations.append((NPCsprite.x, NPCsprite.y))
    return NPClocations

# move to the proper location to pick up the next NPC about to fall
def move(dir1, dir1Release, dir2, dir2Release):
    previousScore = getScore()
    emu.send_input(dir1)
    emu.tick()
    emu.send_input(dir2)
    emu.tick()
    emu.send_input(dir1Release)
    emu.tick()
    emu.send_input(dir2Release)
    while ((previousScore == getScore())): # do not move until you've picked up this NPC
        emu.tick()

# navigate to Fire game
for _ in range(480):
    emu.tick()
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)
for _ in range(240):
    emu.tick()
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
for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)
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
for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
for _ in range(60):
    emu.tick()
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)

while not emu.tick():
    # sprite identifer for the NPC characters range from 16 - 23 and 32 - 39
    # 32 - 39 is just the "bottom half" of the character, so we don't need it for finding their locations
    # we can iterate by 2 because the NPC is 2 sprites wide

    # manSpriteIndices = emu.botsupport_manager().sprite_by_tile_identifier(list(range(16,24,2)))
    # NPClocations = (getNPClocations(manSpriteIndices))
    # if(NPClocations):
    #     # print(NPClocations)
    #     if (32, 25) == NPClocations[0]:
    #         move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT, WindowEvent.PRESS_ARROW_UP, WindowEvent.RELEASE_ARROW_UP)
    #     elif (80, 25) == NPClocations[0]:
    #         move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT, WindowEvent.PRESS_ARROW_UP, WindowEvent.RELEASE_ARROW_UP)
    #     elif (72, 89) == NPClocations[0]:
    #         move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT, WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN)
    #     elif (120, 89) == NPClocations[0]:
    #         move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT, WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN)   
    pass