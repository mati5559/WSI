import argparse
from utils import loadImagesData
from neural_network import NeuralNetwork

# Configure parser and get parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Neural network training example')

    ttGroup = parser.add_mutually_exclusive_group(required=True)
    ttGroup.add_argument('--test', action="store_true", help="Test neural network")
    ttGroup.add_argument('--train', action="store_true", help="Generate and train neural network")

    trainGroup = parser.add_argument_group('Training options')
    trainGroup.add_argument('--layers', type=int, default=3, help="Amount of hidden layers (default: 3)")
    trainGroup.add_argument('--lWidth', type=int, default=50, metavar="WIDTH", help="Amount of neurons in one hidden layer (default: 50)")
    trainGroup.add_argument('-o', type=str, metavar="FILENAME", help="File name where to save generated neural network")


    parser.add_argument('-i', type=str, metavar="FILENAME", help="File name with saved neural network, that will be used")
    parser.add_argument('--datafile', type=str, metavar="FILENAME", help="Name of a file which contains data to test or train neural network", required=True)
    parser.add_argument('--labelfile', type=str, metavar="FILENAME", help="Name of a file which contains labels of images", required=True)

    args = parser.parse_args()

    if((args.test == True) & (args.i is None)):
        print("You need to specify input file when testing neural network (argument -i)")
        exit(1)

    return args



if __name__ == "__main__":
    args = getArguments()

    images, labels = loadImagesData(args.datafile, args.labelfile)

    if(args.train == True):
        network = None
        if args.i is None:
            network = NeuralNetwork(args.lWidth, args.layers, 784)
        else:
            network = NeuralNetwork(filename=args.i)
        

    if(args.test == True):
        network = NeuralNetwork(filename=args.i)
