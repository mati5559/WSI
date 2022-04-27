import random

class Graph:
    def generateRandom(self, nodesNumber, fillFactor):
        self.nodes = []

        # Generatring nodes
        for _ in range(0, nodesNumber):
            self.nodes.append({
                "x": int(random.uniform(0, 1000)),
                "y": int(random.uniform(0, 1000)),
                "connections": []
            })

        # Generating connections between nodes
        for index, node in enumerate(self.nodes):
            for i in range(0, nodesNumber):
                if(i!=index):
                    if((i not in node["connections"]) & (random.random()<fillFactor)):
                        node["connections"].append(i)
                        self.nodes[i]["connections"].append(index)

