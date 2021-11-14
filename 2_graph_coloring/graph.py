import random
import json

class Graph:
    def fromJSON(self, input):
        input = json.loads(input)
        self.nodes = input.nodes
        self.colors = input.colors


    def toJSON(self):
        return json.dumps({"nodes": self.nodes, "colors": self.colors})


    def generateRandom(self, nodesNumber, fillFactor):
        self.nodes = []
        self.colors = []
        
        # Generatring nodes and colors
        for _ in range(0, nodesNumber):
            self.nodes.append({
                "x": random.uniform(0, 1000),
                "y": random.uniform(0, 1000),
                "connections": []
            })
            self.colors.append(int(random.uniform(0, nodesNumber)))

        # Generating connections between nodes
        for index, node in enumerate(self.nodes):
            for i in range(0, nodesNumber):
                if(i!=index):
                    if((i not in node["connections"]) & (random.random()<fillFactor)):
                        node["connections"].append(i)
                        self.nodes[i]["connections"].append(index)
    
