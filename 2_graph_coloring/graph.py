import random
import json

class Graph:
    def __init__(self, nodes=[]):
        if(type(nodes) is str):
            nodes = json.loads(nodes)
        self.nodes = nodes


    def generateRandom(self, nodesNumber, fillFactor):
        self.nodes = []
        for i in range(0, nodesNumber):
            connections = []

            for x in range(0, nodesNumber):
                if((random.random()<fillFactor) & (x!=i)):
                    connections.append(x)

            self.nodes.append({
                "x": random.uniform(0, 1000),
                "y": random.uniform(0, 1000),
                "color": 1,
                "connections": connections
            })


    def toJSON(self):
        return json.dumps(self.nodes)


    
