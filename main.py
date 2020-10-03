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

emu.set_emulation_speed(0)
assert emu.cartridge_title() == "G&W GALLERY" # do not proceed if the is not Game & Watch Gallery

for _ in range(360):
    emu.tick()
print("press A")
emu.send_input(WindowEvent.PRESS_BUTTON_A)
for _ in range(12):
    emu.tick()
emu.send_input(WindowEvent.RELEASE_BUTTON_A)

for _ in range(180):
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

def getScore():
    score = 0
    # player's score is located at this location
    score += (emu.get_memory_value(0xC114))
    score += (emu.get_memory_value(0xC113)) * 10
    score += (emu.get_memory_value(0xC112)) * 100
    return score

def getMissCount():
    return int(emu.get_memory_value(0xC115))

# while not emu.tick():
#     # print(getScore())
#     pass

def getNPClocations(spriteList):
    topNPCs = []
    bottomNPCs = []
    for sublist in spriteList:
        for spriteIndex in sublist:
            NPCsprite = emu.botsupport_manager().sprite(spriteIndex)
            if NPCsprite.y < 50:
                topNPCs.append((NPCsprite.x, NPCsprite.y))
            else:
                bottomNPCs.append((NPCsprite.x, NPCsprite.y))
    return topNPCs, bottomNPCs

def move(dir1, dir1Release, dir2, dir2Release):
    previousScore = getScore()
    misses = getMissCount()
    emu.send_input(dir1)
    emu.tick()
    emu.send_input(dir2)
    emu.tick()
    emu.send_input(dir1Release)
    emu.tick()
    emu.send_input(dir2Release)
    # while (previousScore == getScore()): # do not move until you've picked up this NPC
    #     emu.tick()
    #     if misses != getMissCount(): # if player missed
    #         return

for _ in range(120):
    emu.tick()

manSpriteIndices = emu.botsupport_manager().sprite_by_tile_identifier(list(range(16,24,2)))
topLocations, bottomLocations = getNPClocations(manSpriteIndices)
lastTop = topLocations.copy()
lastBottom = bottomLocations.copy()
while True:
    # emu.tick()
    # sprite identifer for the NPC characters range from 16 - 23 and 32 - 39
    # 32 - 39 is the "bottom half" of 16 - 23, so we don't need it for finding their locations
    # we can iterate by 2 because the NPC is 2 sprites wide
    manSpriteIndices = emu.botsupport_manager().sprite_by_tile_identifier(list(range(16,24,2)))
    
    
    potentialTopLocations, potentialBottomLocations = getNPClocations(manSpriteIndices)
    if potentialTopLocations:
        # if topLocations:
        #     if topLocations != lastTop:
                # lastTop = topLocations
        topLocations = potentialTopLocations
    if potentialBottomLocations:
        # if bottomLocations:
        #     if bottomLocations != lastBottom:
                # lastBottom = bottomLocations
        bottomLocations = potentialBottomLocations
    print(lastBottom, bottomLocations, bottomLocations != lastBottom)
    # if ((topLocations != lastTop) & bool(topLocations)):
    nextMovementBottom = None
    if topLocations != lastTop:
        nextMovementBottom = True
    elif bottomLocations != lastBottom:
        nextMovementBottom = False

    if potentialBottomLocations:
        if bottomLocations:
            if bottomLocations != lastBottom:
                lastBottom = bottomLocations
    if potentialTopLocations:
        if topLocations:
            if topLocations != lastTop:
                lastTop = topLocations
    
    # print(nextMovementBottom)
    
    if nextMovementBottom:
        if (72, 89) in bottomLocations:
            move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT, WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN)
        elif (120, 89) in bottomLocations:
            move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT, WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN)
    else:
        if (32, 25) in topLocations:
            move(WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT, WindowEvent.PRESS_ARROW_UP, WindowEvent.RELEASE_ARROW_UP)
        elif (80, 25) in topLocations:
            move(WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT, WindowEvent.PRESS_ARROW_UP, WindowEvent.RELEASE_ARROW_UP)
    emu.tick()
    # if getMissCount():
    #         print(getMissCount())
    
    