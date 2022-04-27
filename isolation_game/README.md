# Isolation game </br>

This is simple interactive isolation game made to implement and show how minimax alhorithm works. You can move by one field at each direction. Fields visited by one of players are not accessible and you can't move on them.You win when oponent has no legal moves. </br>
Projest contains also "100_test.py", that is a script made for testing algorithms. It runs the game 100 times with 2 computer players and shows how many times each of the players won. </br>

## Usage </br>
```
python3 ./main.py [-h] [--depth1 DEPTH1] [--depth2 DEPTH2] height width PLAYER1 PLAYER2 X1 Y1 X2 Y2

Simple isolation game

positional arguments:
  height           Height of the board
  width            Width of the board
  PLAYER1          Player 1 type. You can choose from: "human", "random", "minimax"
  PLAYER2          Player 2 type. You can choose from: "human", "random", "minimax"
  X1               X coordinate of player 1 start position
  Y1               Y coordinate of player 1 start position
  X2               X coordinate of player 2 start position
  Y2               Y coordinate of player 2 start position

optional arguments:
  -h, --help       show this help message and exit
  --depth1 DEPTH1  Maximum depth of game tree for player 1. Used with minimax algorithm. Default: 10
  --depth2 DEPTH2  Maximum depth of game tree for player 2. Used with minimax algorithm. Default: 15
```
</br>

Game is fully adjustable, so you can change dimensions of board, starting positions and type of players.</br>
You can for example play with computer, that makes random moves (random), with "inteligent" computer (minimax) or with friend (human).</br>
Game computer vs computer is also possible.</br></br>

Warning: High value of depth parameter can make game very slow.