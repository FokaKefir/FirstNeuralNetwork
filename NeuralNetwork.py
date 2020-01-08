
class NeuralNetwork:

    # region 1. Init Object

    def __init__(self, numberOfLayers, layersSize, biases):
        self.numberOfLayers = numberOfLayers
        self.layersSize = layersSize
        self.biases = biases

    # endregion

    # region 2. Creat the Neural Network and Weight matrix

    def creatNeuralNetwork(self):
        id = 0
        self.neuronLayers = []
        for index in range(self.numberOfLayers):
            layerSize = self.layersSize[index]
            bias = self.biases[index]
            newNeuronLayer = NeuronLayer(layerSize, bias, id)
            newNeuronLayer.creatLayer()
            self.neuronLayers.append(newNeuronLayer)

            id = newNeuronLayer.getActuallyId()

        self.numberOfNeurons = id

    def creatingWeights(self):
        self.weights = [[0 for j in range(self.numberOfNeurons)] for i in range(self.numberOfNeurons)]

    # endregion

    # region 3. Connecting neurons

    def connectingTwoLayer(self, layer1, layer2):
        neurons1 = layer1.getNeurons()
        neurons2 = layer2.getNeurons()
        w = 0.15
        for neuronFromLayer1 in neurons1:
            for neuronFromLayer2 in neurons2:
                neuronId1 = neuronFromLayer1.getId()
                neuronId2 = neuronFromLayer2.getId()
                self.setWeightBetweenTwoNeuron(neuronId1, neuronId2, w)
                self.setWeightBetweenTwoNeuron(neuronId2, neuronId1, w)
                w += 0.05

    def connectingNeurons(self):
        for i in range(self.numberOfLayers - 1):
            layer1 = self.getLayerByIndex(i)
            layer2 = self.getLayerByIndex(i + 1)
            self.connectingTwoLayer(layer1, layer2)

    # endregion

    # region 4. Calculations
    def calculatingNeuronsBetweenTwoLayer(self, layerIn, layerOut):
        neuronsIn = layerIn.getNeurons()
        neuronsOut = layerOut.getNeurons()

        for neuronOut in neuronsOut:

            neuronOutId = neuronOut.getId()
            for neuronIn in neuronsIn:
                neuronInId = neuronIn.getId()


    def calculatingValuesOfNeurons(self):
        for i in range(self.numberOfLayers):
            layerIn = self.getLayerByIndex(i)
            layerOut = self.getLayerByIndex(i + 1)
            self.calculatingNeuronsBetweenTwoLayer(layerIn, layerOut)

    # endregion

    # region 5. Getters and Setters
    def setWeightBetweenTwoNeuron(self, nId1, nId2, weight):
        self.weights[nId1][nId2] = weight

    def getLayerByIndex(self, index):
        return self.neuronLayers[index]

    def getWeightBetweenTwoNeuron(self, nId1, nId2):
        return self.weights[nId1][nId2]

    # endregion

    # region 6. Prints

    def printWeights(self):
        for i in range(self.numberOfNeurons):
            for j in range(self.numberOfNeurons):
                val = self.weights[i][j]
                print(val, end=' ')
            print()

    # endregion++

class NeuronLayer:

    # region 1. Init Object
    def __init__(self, numberOfNeurons, bias, actuallyId):
        self.numberOfNeurons = numberOfNeurons
        self.actuallyId = actuallyId
        self.bias = bias

    # endregion

    # region 2. Creat Layers

    def creatLayer(self):
        self.neurons = []
        for i in range(self.numberOfNeurons):
            newNeuron = Neuron(self.actuallyId)
            self.neurons.append(newNeuron)
            self.actuallyId += 1

    # endregion

    # region 3. Getters and Setters

    def getActuallyId(self):
        return self.actuallyId

    def getNeurons(self):
        return self.neurons

    def setActuallyId(self, newId):
        self.actuallyId = newId

    # endregion

class Neuron:

    # region 1. Init Object
    def __init__(self, id, value = None):
        self.id = id
        if(value == None):
            self.value = 0
        else:
            self.value = value

    # endregion

    # region 2. Getters and Setters

    def getId(self):
        return self.id
    def getValue(self):
        return self.value
    def setId(self, newId):
        self.id = newId
    def setValue(self, newValue):
        self.value = newValue

    # endregion

def main():
    numberOfLayers = 3
    layersSize = [2, 2, 2]
    biases = [0, 0.35, 0.60]
    neuralNetwork = NeuralNetwork(numberOfLayers, layersSize, biases)
    neuralNetwork.creatNeuralNetwork()
    neuralNetwork.creatingWeights()
    neuralNetwork.connectingNeurons()


main()