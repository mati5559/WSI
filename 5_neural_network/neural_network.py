import random
import math
import decimal
import json

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
    def __init__(self, layerWidth=None, layersNumber=None, inputsNumber=None, filename=None):
        if filename is not None:
            self.loadFromFile(filename)
            return

        self.layers = []
        self.layers.append([])

        for _ in range(0, layerWidth):
            self.layers[0].append(Neuron(sigmaFunction, None, inputsNumber))
        
        for _ in range(1, layersNumber):
            layer = []
            
            for _ in range(0, layerWidth):
                layer.append(Neuron(sigmaFunction, self.layers[-1], None))
            
            self.layers.append(layer)

        self.outputNode = Neuron(linearFunction, self.layers[-1])

    def getResult(self, input) -> int:
        previousLayerResult = input
        for layer in self.layers:
            nextResults = []

            for neuron in layer:
                nextResults.append(neuron.getResult(previousLayerResult))
            previousLayerResult = nextResults
        
        return self.outputNode.getResult(previousLayerResult)
    
    def saveToFile(self, fileName):
        weights = []
        for layer in self.layers:
            weightsLayer = []
            for neuron in layer:
                weightsLayer.append(neuron.weights)
            weights.append(weightsLayer)

        weights.append([self.outputNode.weights])
        
        with open(fileName, 'w') as file:
            json.dump({
                "weights":weights
            }, file)

    def loadFromFile(self, filename):
        weights = None
        with open(filename, 'r') as file:
            weights = json.load(file)['weights']

        self.layers = []
        self.layers.append([])


        firstLayer = weights.pop(0)
        for neuronWeights in firstLayer:
            newNeuron = Neuron(sigmaFunction, None, len(neuronWeights))
            newNeuron.weights = neuronWeights
            self.layers[0].append(newNeuron)
        
        for _ in range(0, len(weights)-1):
            layer = weights.pop(0)
            newLayer = []
            for neuronWeights in layer:
                newNeuron = Neuron(sigmaFunction, self.layers[-1])
                newNeuron.weights = neuronWeights
                newLayer.append(newNeuron)

            self.layers.append(newLayer)

        self.outputNode = Neuron(linearFunction, self.layers[-1])
        self.outputNode.weights = weights[-1][0]
            
        
