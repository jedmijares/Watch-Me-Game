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
            if True: #NPCsprite.x in {32, 80, 72, 120}: # these are the only x positions that NPCs about to fall appear
                NPClocations.append((NPCsprite.x, NPCsprite.y))
    return NPClocations

# move to the proper location to pick up the next NPC about to fall
def move(dir1, dir1Release, dir2 = None, dir2Release = None):
    emu.send_input(dir1)
    emu.tick()
    emu.send_input(dir1Release)
    emu.tick()

# navigate to Fire game
for _ in range(360):
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
emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)
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

misses = 0
while not emu.tick():
    # sprite identifer for the NPC characters range from 65 - 68 for the left person, 96 - 99 for the center, and 120 - 123 for the right
    manSpriteIndices = emu.botsupport_manager().sprite_by_tile_identifier([65, 96, 120])
    NPClocations = (getNPClocations(manSpriteIndices))
    if(NPClocations):
        # print(NPClocations)

        # these are the possible x/y coordinates of NPCs that are about to hit the ground
        if (24, 102) == NPClocations[0]:
            move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT)
            move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT)
        elif (64, 102) == NPClocations[0]:
            move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT)
            move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT)
            move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT)
        elif (102, 100) == NPClocations[0]:
            move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT)
            move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT)
    
    # if misses != getMissCount():
    #     misses += 1
    #     print("miss", misses)