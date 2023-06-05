# TetrisTaltech
Tetris game for taltech final course 2022/2023

## Members
- Marten Mehide
- Ronja Niine Lõhmuste
- Joosep Lukin

## Playing the game
To play the game, first install all requirements by running `python3 -m pip install -r requirements.txt`
Then start the game with `python3 main.py`


## Game logic
Every game element is treated as an object, as well as the game itself.
The game has 4 states (also objects):
1. Title screen state
  > The title screen state just displays the `PLAY` and `QUIT` buttons and the buttons are clickable with the keyboard.
2. Play state
  > The play state is the game itself, with blocks falling from the top of the screen. The game is basic Tetris - the blocks are the same and you can also rotate them or swap a piece to storage to use later. Future pieces are also displayed. When playing a 1VS1 game, clearing a row will send that row to the bottom of the other player's rows, having 1 hole that must be filled in order to clear it. The game ends when either player dies.
3. Game over state
  > The game over state displays the stats after the game is finished: the number of rows each player cleared and their score. If a 1VS1 game was played, the winner is also displayed. There is also an option to return to title screen.

 
## TODO

### Important features:
- [x] Create basic game engine
  - [x] Create rendering engine
  - [x] Create basic state logic
  - [x] Create Title screen state core logic
  - [x] Create Player settings state core logic
  - [x] Create Play state core logic
  - [x] Create Game over state core logic
- [x] Create game functions
  - [x] Create game element basic logic
  - [x] Create tetris blocks logic
- [x] Title screen state
- [ ] Player selection state
- [ ] Play state
- [ ] Game over state


### Optional features
- [ ] Add music
- [ ] Add animation effects
- [ ] Train neural network to play Tetris :)

Panna plokid kiiremini kukkuma, mida kauem mäng kestab.
Teha nii, et tühikut vajutades, kukub plokk kohe kõige lõppu. DONE VIG
Teha nii, et allanoolt all hoides kukub plokk kiiremini. DONE NIG
Valida head värvid plokkidele.
Lisada mängu pausile panemise võimalus.
Lisada skoori trackimine.
Lisada ploki hoiustamine.
Lisada võimalus näha, mis plokid tulevikus tulevad.
