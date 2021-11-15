#!/bin/python3

import matplotlib.pyplot as plt
import argparse
import coloring
import json
from graph import Graph

colorMap = ['olive', 'aquamarine', 'lightgreen', 'deepskyblue', 'red', 'yellow', 'grey', 'pink', 'cyan', 'hotpink',
            'navy', 'lightcoral', 'turquoise', 'deeppink', 'violet', 'fuchsia', 'orangered', 'orange', 'gold',
            'brown', 'blue', 'seagreen', 'blueviolet', 'lawngreen', 'indigo', 'darkcyan', 'mediumpurple', 'black',
            'royalblue', 'green']


# Configuring argument parser and return parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Graph coloring problem solving using evolutionary algorithm.')

    giGroup = parser.add_mutually_exclusive_group(required=True)
    giGroup.add_argument('-r', metavar="FILENAME", type=str, help="Read graph from file")

    giGroup.add_argument('-g', action='store_true', help='Generate random graph')
    parser.add_argument('--vertex', type=int, default=25, help="Number of vertex of generated graph (default 25)")
    parser.add_argument('--fillfactor', type=float, default=0.4, help="Determinates how many of the possible edges graph will have (between 0 and 1, default 0.4)")

    parser.add_argument('-c', action="store_true", help="Color graph using evolutionary algorithm")
    parser.add_argument('--ps', type=int, default=50, metavar="SIZE", help="Population size (default 50)")
    parser.add_argument('--iter', type=int, default=1000, metavar="ITERATIONS", help="Amount of iterations (default 1000)")
    parser.add_argument('--pm', type=float, default=0.2, help="Mutation plausibility (default 0.2)")

    parser.add_argument('-s', action="store_true", help="Show final graph")

    parser.add_argument('-o', type=str, metavar="FILENAME", help="Save final graph to specified file")

    return parser.parse_args()


# Show graph using matplotlib
def showGraph(graph, lineColor="black", pointSize=50, colorsIndexes=None):
    x = []
    y = []
    colors = []

    for node in graph.nodes:
        x.append(node["x"])
        y.append(node["y"])
        for connection in node["connections"]:
            plt.plot([node["x"], graph.nodes[connection]["x"]],
                     [node["y"], graph.nodes[connection]["y"]], c=lineColor)


    if((colorsIndexes is None) or (max(colorsIndexes) >= len(colorMap))):
        colors = ["red" for _ in range(0, len(x))]
    else:
        for colorIndex in colorsIndexes:
            colors.append(colorMap[colorIndex])

    plt.scatter(x, y, s=pointSize, c=colors)
    plt.show()


if __name__ == "__main__":
    arguments = getArguments()
    graph = Graph()
    colors = None

    if arguments.g:
        graph.generateRandom(arguments.vertex, arguments.fillfactor)

    if arguments.r:
        with open(arguments.r, "r") as file:
            data = json.load(file)
            graph.nodes = data["graph"]
            colors = data["colors"]
            file.close()

    if arguments.c:
        colors, grade = coloring.colorGraph(graph, arguments.ps, arguments.iter, arguments.pm, int(arguments.vertex/5)+1)
        print("Solution quality: " + str(grade) + " (lower is better, should be at most equal to vertices number)")

    if arguments.s:
        showGraph(graph, colorsIndexes=colors)

    if arguments.o:
        with open(arguments.o, "w") as file:
            json.dump({"graph": graph.nodes, "colors": colors}, file)
            file.close()
