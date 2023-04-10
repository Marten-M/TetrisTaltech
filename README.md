# TetrisTaltech
Tetris game for taltech final course 2022/2023

## Members
- Mjäuten Mehide
- Ronja Niine Lõhmuste
- Joosep Lukin

## Playing the game
To play the game, first install all requirements by running `python3 -m pip install -r requirements.txt`
Then start the game with `python3 main.py`


## Game logic
Every game element is treates as an object, as well as the game itself.
The game has 4 states (also objects):
1. Title screen state
  > The title screen state just displays the `PLAY` and `QUIT` buttons and the buttons are clickable either with the keyboard or the mouse.
2. Player settings state
  > The player settings state is the phase where the number of players (1 or 2) is chosen as well as names for them.
3. Play state
  > The play state is the game itself, with blocks falling from the top of the screen. The game is basic Tetris - the blocks are the same and you can also rotate them or swap a piece to storage to use later. Future pieces are also displayed. When playing a 1VS1 game, clearing a row will send that row to the bottom of the other player's row's, having 1 hole that must be filled in order to clear it. The game ends when either player dies.
4. Game over state
  > The game over state displays the stats after the game is finished - the number of rows each player cleared and their score. If a 1VS1 game was played, the winner is also displayed. There is also an option to return to title screen.

 
## TODO

### Important features:
- [x] Create basic game engine
  - [x] Create rendering engine
  - [x] Create basic state logic
  - [x] Create Title screen state core logic
  - [x] Create Player settings state core logic
  - [x] Create Play state core logic
  - [x] Create Game over state core logic
- [ ] Create game functions
  - [ ] Create game element basic logic
  - [ ] Create tetris blocks logic
- [ ] Title screen state
- [ ] Player selection state
- [ ] Play state
- [ ] Game over state


### Optional features
- [ ] Add music
- [ ] Add animation effects
- [ ] Train neural network to play Tetris :)
