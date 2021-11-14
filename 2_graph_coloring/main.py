import matplotlib.pyplot as plt
import argparse
from graph import Graph



# Configuring argument parser and return parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Graph coloring problem solving using evolutionary algorithm.')
    
    giGroup = parser.add_mutually_exclusive_group(required=True)
    giGroup.add_argument('-r', metavar="FILENAME", type=str, help="Read graph from file")

    giGroup.add_argument('-g', action='store_true', help='Generate random graph')
    parser.add_argument('--vertex', type=int, default=25, help="Number of vertex of generated graph (default 25)")
    parser.add_argument('--fillfactor', type=float, default=0.4, help="Determinates how many of the possible edges graph will have (between 0 and 1, default 0.4)")

    parser.add_argument('-s', action="store_true", help="Show final graph")

    parser.add_argument('-o', type=str, metavar="FILENAME", help="Save final graph to specified file")

    return parser.parse_args()


# Show graph using matplotlib
def showGraph(graph, lineColor="black", pointSize=30, pointColor="red", colorTable=None):
    x = []
    y = []
    colors = []

    for node in graph.nodes:
        x.append(node["x"])
        y.append(node["y"])
        for nodeIndex, connection in enumerate(node["connections"]):
            if(connection<nodeIndex):
                plt.plot([node["x"], graph.nodes[connection]["x"]],
                         [node["y"], graph.nodes[connection]["y"]], c=lineColor)


    if colorTable is None:
        colors = [pointColor for _ in range(0, len(x))]
    else:
        for colorIndex in graph.colors:
            colors.append(colorTable[colorIndex])

    plt.scatter(x, y, s=pointSize, c=colors)
    plt.show()


if __name__ == "__main__":
    arguments = getArguments()
    graph = Graph()

    if arguments.g:
        graph.generateRandom(arguments.vertex, arguments.fillfactor)

    if arguments.s:
        showGraph(graph) #, colorTable=["red", "green", "blue", "yellow", "cyan"])
