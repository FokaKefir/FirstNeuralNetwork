import time
from gui.neuralnetwrok import NeuralNetwork


def training(neuralNetwork):
    while(True):
        neuralNetwork.calculatingValuesOfNeurons()
        neuralNetwork.calculatingError()
        neuralNetwork.printNameAndValue()
        neuralNetwork.backPropagation()
        time.sleep(0.1)

def main():
    numberOfLayers = 3
    layersSize = [2, 2, 2]
    biases = [0, 0.35, 0.60]
    neuralNetwork = NeuralNetwork.NeuralNetwork(numberOfLayers, layersSize, biases)
    neuralNetwork.creatNeuralNetwork()
    neuralNetwork.creatingWeights()
    neuralNetwork.addingWeights()
    neuralNetwork.addingOutputNeuronsName(["false", "true"])
    neuralNetwork.addingInput([0.05, 0.1], "true")
    training(neuralNetwork)


main()
