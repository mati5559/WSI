# Q-uber</br>

This project is an example how q-learning algorithm works. First it generates random maze, random start and end positions (you can use fixed positions). Next program checks if there is any possible route between start and end positions using DFS algorithm. If there is no possible route between two points, program makes new random maze. Then the q-learning algorithm controlling a "car" in the maze tries to find the shortest route between start and end points. Player loses when he hits obstacles and the game is ended. 

## Usage</br>
```
pytnon3 main.py [-h] [--start START START] [--end END END] [--seed SEED] (--random | --quber) [--print] [--epoch EPOCH] [--beta BETA] [--df DF] [--test X] N

Finding best route from start to end with O-Learning algorithm - "Q-Uber"

positional arguments:
  N                    Board size

optional arguments:
  -h, --help           show this help message and exit
  --start START START  Coordinates of start position
  --end END END        Coordinates of end position
  --seed SEED          Seed for random generator
  --random             Use random driver
  --quber              Use driver, that uses Q-learning algorithm
  --print              Print board with example run in console
  --epoch EPOCH        Number of epochs for QUber (default 500)
  --beta BETA          Beta parameter for QUber (default 1)
  --df DF              Discount factor for QUber (default 1)
  --test X             Test driver X times
```
</br>
You can also choose between inteligent driver and driver, that chooses random moves. </br>
The --test X parameter runs program X times and counts how many times driver reached goal (on the same board)</br>