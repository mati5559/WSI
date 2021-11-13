import matplotlib.pyplot as plt
import argparse
from graph import Graph


# Configuring argument parser and return parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Graph coloring problem solving using evolutionary algorithm.')
    
    giGroup = parser.add_mutually_exclusive_group(required=True)
    giGroup.add_argument('-g', action='store_true', help='Generate random graph')
    giGroup.add_argument('-r', metavar="FILENAME", type=str, help="Read graph from file")

    parser.add_argument('--vertex', type=int, default=25, help="Number of vertex of generated graph (default 25)")
    parser.add_argument('--fillfactor', type=float, default=0.4, help="Determinates how much of the possible edges graph will have (between 0 and 1)")

    parser.add_argument('-s', action="store_true", help="Only show graph, do not run evolutionary algorithm")

    parser.add_argument('-o', type=str, metavar="FILENAME", help="Save graph to specified file")

    return parser.parse_args()


# Show graph using matplotlib
def showGraph(graph, lineColor="black", pointSize=60, pointColor="red", colorTable=None):
    x = []
    y = []
    colors = []

    for node in graph.nodes:
        x.append(node["x"])
        y.append(node["y"])
        colors.append(pointColor if colorTable is None else colorTable[node["color"]])
        for connection in node["connections"]:
            plt.plot([node["x"], graph.nodes[connection]["x"]],
                     [node["y"], graph.nodes[connection]["y"]], c=lineColor)


    plt.scatter(x, y, s=pointSize, c=colors)
    plt.show()


if __name__ == "__main__":
    arguments = getArguments()
    print(arguments)
    exit()
    testGraph = Graph()
    testGraph.generateRandom(10, 0.1)
    showGraph(testGraph)
