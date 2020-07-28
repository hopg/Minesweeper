# Minesweeper

A Minesweeper game that includes two different grid sizes that the player can choose from. 

The aim of the game is to reveal all tiles on the board that do not contain a mine. 

The player selects a tile by choosing a number on the grid; number 1 refers to the top right square.

Upon selecting a tile, one of either two things occur:
- A number is shown which tells the player how many mines are adjacent to the tile selected, that is up, down, left, right and diagonal.
- An X is shown, which is a mine and thus the game ends.

A player can also plant flags by entering ```Fi``` where ```i``` correpsonds the position of where they would like to the flag to be placed.

The flags are used as a way of keeping track where potential mines may be located. 

The player must continue to reveal the tiles that do not contain a mine to win the game.

There is also the option to choose from two grid sizes:
- 3 x 4 which contains 3 mines
- 4 x 5 which contains 5 mines

Naturally, the 4 x 5 grid is tougher than the 3 x 4 grid.


#### Required Modules:
- random
- IPython.display


#### Known Issues:
- ~~Can select negative number for positions~~
- ~~No current check for a number that is out of bounds for the grid~~
- The flag count can go below 0, this is done intentionally as this is in line with the original minesweeper game.
- Can use any word beginning with 'y' or 'n' to say yes or no; no plan to fix this as this makes debugging easier!
