# Graph coloring

This program solves problem "how to color all the vertices of the graph so that there are no two connected vertices of the same color".</br>
I solved this problem with evolutionary algorithm.

### Usage</br>
```
python3 ./main.py [-h] (-r FILENAME | -g) [--vertex VERTEX] [--fillfactor FILLFACTOR] [-c] [--ps SIZE] [--iter ITERATIONS] [--pm PM] [-s] [-o FILENAME]

Graph coloring problem solving using evolutionary algorithm.

optional arguments:
  -h, --help            show this help message and exit
  -r FILENAME           Read graph from file
  -g                    Generate random graph
  --vertex VERTEX       Number of vertex of generated graph (default 25)
  --fillfactor FILLFACTOR
                        Determinates how many of the possible edges graph will have (between 0 and 1, default 0.4)
  -c                    Color graph using evolutionary algorithm
  --ps SIZE             Population size (default 50)
  --iter ITERATIONS     Amount of iterations (default 1000)
  --pm PM               Mutation plausibility (default 0.2)
  -s                    Show final graph
  -o FILENAME           Save final graph to specified file
```