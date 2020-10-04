# Watch Me Game

This is my submission for VandyHacks 2020! The theme is retro, so I figured I'd take my project all the way back to 1981. Watch Me Game is a bot to play [Game & Watch Gallery](https://en.wikipedia.org/wiki/Game_%26_Watch_Gallery), a retro collection of even more retro handheld electronic games. It's written in Python using [PyBoy](https://github.com/Baekalfen/PyBoy).

## Process

Step one was to figure out how to process data in the game. PyBoy comes with wrappers that facilitate this for a few games, but Game & Watch Gallery is unfortunately not one of them. So, I dug into the game myself to figure out how to pull out that info into my script.

Finding integer values like the current score was simple enough - I used [VBA-M's](https://github.com/visualboyadvance-m/visualboyadvance-m) cheat engine to find the memory location where the values were held and was able to use PyBoy to read that data. Grabbing the position of various characters on the screen, however, was more troublesome. For a little while, I fumbled around trying to find another memory location storing the position of each character would be saved, but I didn't have any luck as I had no idea how that value might be represented.

<img src="https://github.com/jedmijares/Watch-Me-Game/blob/main/media/spriteDebugging.png" alt="Debug Interface" width="600"/>

Thankfully, PyBoy offers some helpful debugging tools that let me proceed. By observing the sprite and tile data tables as I played the game myself, I could find the identifiers for each character's sprites and pass that through PyBoy to find the location of each character in real time.

### Bots

The first bot I wrote was for Manhole. This one uses the sprite positions collected above to determine if a character is about to fall off the bridge, and positions the player to catch them if so. This one can play the game indefinitely.

<img src="https://github.com/jedmijares/Watch-Me-Game/blob/main/media/manhole.gif" width="250" />

The second one is for Fire. It operates very similarly, but this one usually only manages to score a few dozen points before losing the game.

<img src="https://github.com/jedmijares/Watch-Me-Game/blob/main/media/fire.gif" width="250" />

## Next Steps

Initially I was interested in developing neural nets to play some of the games in this collection, but I ended up deciding that was out of my purview for this weekend. If I revisit this project in the future I'll be reconsidering writing another bot implementing that.
