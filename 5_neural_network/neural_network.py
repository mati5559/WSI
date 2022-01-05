import random
import math
import decimal
def sigmaFunction(x):
    return int(1/(1+(decimal.Decimal(math.e)**(decimal.Decimal(-x)))))

def linearFunction(x):
    return x

class Neuron:
    def __init__(self, outputFunction, children=None, inputsNumber=None):
        if (children is None) & (inputsNumber is None):
            raise ValueError("Children and inputsNumber not specified")

        self.outputFunction = outputFunction
        self.children = children
        self.weights = []

        weightsNumber = len(children) if children is not None else inputsNumber

        # Last weight is bias
        for _ in range(0, weightsNumber+1):
            self.weights.append(random.uniform(-10, 10)) 


    def getResult(self, input):
        sum = self.weights[-1] # bias
            
        for index in range(0, len(input)):
            sum += input[index] * self.weights[index]

        return self.outputFunction(sum)

        
class NeuralNetwork:
    def __init__(self, layerWidth, layersNumber, inputsNumber):
        self.layers = []
        self.layers.append([])

        for _ in range(0, layerWidth):
            self.layers[0].append(Neuron(sigmaFunction, None, inputsNumber))
        
        for _ in range(0, layersNumber):
            layer = []
            
            for _ in range(0, layerWidth):
                layer.append(Neuron(sigmaFunction, self.layers[-1], None))
            
            self.layers.append(layer)

        self.outputNode = Neuron(linearFunction, self.layers[-1])

    def getResult(self, input):
        previousLayerResult = input
        for layer in self.layers:
            nextResults = []

            for neuron in layer:
                nextResults.append(neuron.getResult(previousLayerResult))
            previousLayerResult = nextResults
        
        return self.outputNode.getResult(previousLayerResult)
    
