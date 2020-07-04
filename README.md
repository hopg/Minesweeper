# Minesweeper

A Minesweeper game that includes two different grid sizes that the player can choose from. 

The aim of the game is to reveal all tiles on the board that do not contain a mine. 

Upon selecting a tile, by choosing a number on the keyboard, 1 being the first tile, one of either two things occur:
- A number is shown which tells the player how many mines are adjacent to the tile selected, that is up, down, left, right and diagonals.
- A X is shown, which is a mine and thus the game ends.

The player must continue to reveal the tiles that do not contain a mine to win the game.

There is also the option to choose from two grid sizes:
- 3 x 4 which contains 3 mines
- 4 x 5 which contains 5 mines

The 4 x 5 grid is tougher than the 3 x 4 grid.


#### Required Modules:
- random
- IPython.display


#### Known Issues:
- ~~Can select negative number for positions~~
- ~~No current check for a number that is out of bounds for the grid~~
- Can use any word beginning with 'y' or 'n' to say yes or no; no plan to fix this as this makes debugging easier!
