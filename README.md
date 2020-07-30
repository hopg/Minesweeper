# Minesweeper

A Minesweeper game that includes two different grid sizes that the player can choose from. 

## Table of Contents

- [Introduction to Minesweeper](https://github.com/hopg/Minesweeper#Introduction-to-Minesweeper)
- [Features](https://github.com/hopg/Minesweeper#Features)
- [Required Modules](https://github.com/hopg/Minesweeper#Required-Modules)
- [Known Issues](https://github.com/hopg/Minesweeper#Known-Issues)

## Introduction to Minesweeper

The aim of the game is to reveal all tiles on the board that do not contain a mine. 

The player selects a tile by choosing a number on the grid; number 1 refers to the top left square.

Upon selecting a tile, one of either two things occur:
- A number is shown which tells the player how many mines are adjacent to the tile selected, that is up, down, left, right and diagonal.
- An X is shown, which is a mine and thus the game ends.

The player must continue to reveal the all the tiles that do not contain a mine to win the game.

A player can also plant flags by entering ```Fi``` where ```i``` correpsonds the position of where they would like to the flag to be placed. The flags are used as a way of keeping track where potential mines may be located. 

The grid sizes the player can choose from are:
- 3 x 4 which contains 3 mines
- 4 x 5 which contains 5 mines

Naturally, the 4 x 5 grid is tougher than the 3 x 4 grid.

## Features
- Player cannot select a mine on their first turn
- Cannot reveal a tile that has already been revealed
- Unable to enter in a position that is outside the grid area
- Invalid position choices will notify the player
- Entering no position will result in a message informing the player 
- If a flag is on a tile and a flag placed on the same tile, this will remove the flag
- Flags cannot be placed on tiles that are revealed as they cannot be mines
- No flags are placed if chosen outside the grid area
- Invalid flag positions will notify the player
- Running count of the number of flags remaining, total number of flags equates to the number of mines
- Option to replay once a game has ended
- ```Mines()``` class has three magic methods:
  - ```__setitem__```, ```__getitem__``` and ```__iter__```
- ```Mines()``` class has a debugging method ```mine_pos()``` which shows the positions of the mines


## Required Modules
- random
- IPython.display


## Known Issues
- ~~Can select negative number for positions~~
- ~~No current check for a number that is out of bounds for the grid~~
- The flag count can go below 0, this is done intentionally as this is in line with the original minesweeper game.
- Can use any word beginning with 'y' or 'n' to say yes or no; no plan to fix this as this makes debugging easier!
