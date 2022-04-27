# Minimum Finder </br>

This project shows how to find minimum of multi-dimensional function using gradient descent and Newton's methods.</br>


### Usage</br>
```
$ python3 ./minimumFinder.py [-h] [--nm] [--gdm] X Y B iter

positional arguments:
  X           X coordinate of starting point
  Y           Y coordinate of starting point
  B           B parameter for algorithm
  iter        Number of iterations

optional arguments:
  -h, --help  show this help message and exit
  --nm        Show Newton method
  --gdm       Show gradient descent method
```
</br>

X and Y should be between -6 and 6.</br>
B is a "gain" of algorithm. Too high value will cause unstable beahviour of algorithm. Suggested value is 0.01</br>

