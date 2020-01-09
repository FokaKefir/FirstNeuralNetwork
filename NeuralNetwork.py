from math import e

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
        self.weights = []

    # endregion

    # region 3. Adding weights between Neurons

    def addingWeightsBetweenTwoLayer(self, layer1, layer2):
        neurons1 = layer1.getNeurons()
        neurons2 = layer2.getNeurons()
        for neuronFromLayer2 in neurons2:
            for neuronFromLayer1 in neurons1:
                neuronId1 = neuronFromLayer1.getId()
                neuronId2 = neuronFromLayer2.getId()
                self.setWeightBetweenTwoNeuron(neuronId1, neuronId2, self.w)
                self.w += 0.05

    def addingWeights(self):
        self.w = 0.15
        for i in range(self.numberOfLayers - 1):
            layer1 = self.getLayerByIndex(i)
            layer2 = self.getLayerByIndex(i + 1)
            self.addingWeightsBetweenTwoLayer(layer1, layer2)
            self.w += 0.05

    # endregion

    # region 4. Adding input

    def addingInput(self, inputValues):
        self.neuronLayers[0].addingValuesForNeurons(inputValues)

    # endregion

    # region 5. Calculations
    def calculatingNeuronsBetweenTwoLayer(self, layerIn, layerOut):
        neuronsIn = layerIn.getNeurons()
        neuronsOut = layerOut.getNeurons()
        bias = layerOut.getBias()
        for neuronOut in neuronsOut:
            net = 0
            neuronOutId = neuronOut.getId()
            for neuronIn in neuronsIn:
                neuronInId = neuronIn.getId()
                neuronInValue = neuronIn.getValue()
                weight = self.getWeightBetweenTwoNeuron(neuronInId, neuronOutId)
                net += neuronInValue * weight
            net += bias
            out = 1 / (1 + e ** (-1 * net))
            neuronOut.setValue(out)

    def calculatingValuesOfNeurons(self):
        for i in range(self.numberOfLayers-1):
            layerIn = self.getLayerByIndex(i)
            layerOut = self.getLayerByIndex(i + 1)
            self.calculatingNeuronsBetweenTwoLayer(layerIn, layerOut)

    # endregion

    # region 6. Getters and Setters
    def setWeightBetweenTwoNeuron(self, nId1, nId2, weight):
        newElement = {'id1': min(nId1, nId2), 'id2': max(nId1, nId2), 'weight': weight}
        self.weights.append(newElement)

    def getLayerByIndex(self, index):
        return self.neuronLayers[index]

    def getWeightBetweenTwoNeuron(self, nId1, nId2):
        id1 = min(nId1, nId2)
        id2 = max(nId1, nId2)
        for weight in self.weights:
            if(weight['id1'] == id1 and weight['id2'] == id2):
                w = weight['weight']
                return w
        return None

    # endregion

    # region 7. Prints

    def printWeights(self):
        for weight in self.weights:
            print(weight)


    # endregion

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

    # region 3. Adding values for Neurons

    def addingValuesForNeurons(self, values):
        for i in range(self.numberOfNeurons):
            val = values[i]
            self.neurons[i].setValue(val)

    # endregion

    # region 4. Getters and Setters

    def getActuallyId(self):
        return self.actuallyId

    def getNeurons(self):
        return self.neurons

    def getBias(self):
        return self.bias

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
    neuralNetwork.addingWeights()
    neuralNetwork.printWeights()
    neuralNetwork.addingInput([0.05, 0.1])
    neuralNetwork.calculatingValuesOfNeurons()

main()