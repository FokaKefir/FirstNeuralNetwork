from math import e

learningRate = 0.5
class NeuralNetwork:

    # region 1. Init Object

    def __init__(self, numberOfLayers, layersSize, biases):
        self.numberOfLayers = numberOfLayers
        self.layersSize = layersSize
        self.biases = biases

    # endregion

    # region 2. Creat the Neural Network and Weight list

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

        del(self.layersSize)
        del(self.biases)

    def creatingWeights(self):
        self.weights = []

    # endregion

    # region 3. Adding weights between Neurons

    def addingWeightBetweenTwoNeuron(self, nId1, nId2, weight):
        newElement = {'id1': min(nId1, nId2), 'id2': max(nId1, nId2), 'weight': weight, 'derErrorPerOut': 0}
        self.weights.append(newElement)

    def addingWeightsBetweenTwoLayer(self, layer1, layer2):
        neurons1 = layer1.getNeurons()
        neurons2 = layer2.getNeurons()
        for neuronFromLayer2 in neurons2:
            for neuronFromLayer1 in neurons1:
                neuronId1 = neuronFromLayer1.getId()
                neuronId2 = neuronFromLayer2.getId()
                self.addingWeightBetweenTwoNeuron(neuronId1, neuronId2, self.w)
                self.w += 0.05

    def addingWeights(self):
        self.w = 0.15
        for i in range(self.numberOfLayers - 1):
            layer1 = self.getLayerByIndex(i)
            layer2 = self.getLayerByIndex(i + 1)
            self.addingWeightsBetweenTwoLayer(layer1, layer2)
            self.w += 0.05

        del(self.w)

    # endregion

    # region 4. Adding output neurons name

    def addingOutputNeuronsName(self, names):
        layer = self.neuronLayers[self.numberOfLayers - 1]
        neurons = layer.getNeurons()
        for i in range(len(neurons)):
            neurons[i].setName(names[i])

    # endregion

    # region 5. Adding input

    def addingInput(self, inputValues, result):
        self.neuronLayers[0].addingValuesForNeurons(inputValues)
        self.result = result

    # endregion

    # region 6. Forward
    def calculatingNeuronsValueBetweenTwoLayer(self, layerIn, layerOut):
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
        for i in range(self.numberOfLayers - 1):
            layerIn = self.getLayerByIndex(i)
            layerOut = self.getLayerByIndex(i + 1)
            self.calculatingNeuronsValueBetweenTwoLayer(layerIn, layerOut)

    # endregion

    # region 7. Backward

    def calculatingDerErrorPerOut(self, neuronIn, neuronOut, condition, index):
        nOutValue = neuronOut.getValue()

        if (condition):
            if (neuronOut.getName() == self.result):
                target = 0.99
            else:
                target = 0.01
            derErrorPerOut = nOutValue - target

        else:
            derErrorPerOut = 0
            neuronsIndex = self.neuronLayers[index+1].getNeurons()
            for neuronIndex in neuronsIndex:
                derErrorPerOut += self.getDerErrorPerOutBetweenTwoNeuron(neuronOut.getId(), neuronIndex.getId())

        return derErrorPerOut

    def backPropagationBeetwenTwoLayer(self, layerOut, layerIn, condition, index):
        neuronsOut = layerOut.getNeurons()
        neuronsIn = layerIn.getNeurons()

        for neuronOut in neuronsOut:
            for neuronIn in neuronsIn:
                nOutId = neuronOut.getId()
                nInId = neuronIn.getId()

                nOutValue = neuronOut.getValue()
                nInValue = neuronIn.getValue()

                derErrorPerOut = self.calculatingDerErrorPerOut(neuronIn, neuronOut, condition, index)
                derOutPerNet = nOutValue * (1 - nOutValue)
                derNetPerWeight = nInValue

                derErrorPerWeight = derErrorPerOut * derOutPerNet * derNetPerWeight

                newWeight = self.getWeightBetweenTwoNeuron(nInId, nOutId) - learningRate * derErrorPerWeight

                self.setDerErrorPerOutBetweenTwoNeuron(
                    nInId, nOutId, (derErrorPerOut * derOutPerNet * self.getWeightBetweenTwoNeuron(nInId, nOutId)))

                self.setWeightBetweenTwoNeuron(nInId, nOutId, newWeight)


    def backPropagation(self):
        for i in range(self.numberOfLayers-1, 0, -1):
            layerOut = self.neuronLayers[i]
            layerIn = self.neuronLayers[i-1]
            condition = False
            if(i == self.numberOfLayers-1):
                condition = True
            self.backPropagationBeetwenTwoLayer(layerOut, layerIn, condition, i)


    # endregion

    # region 8. Getters and Setters
    def getLayerByIndex(self, index):
        return self.neuronLayers[index]

    def getWeightBetweenTwoNeuron(self, nId1, nId2):
        id1 = min(nId1, nId2)
        id2 = max(nId1, nId2)
        for weight in self.weights:
            if (weight['id1'] == id1 and weight['id2'] == id2):
                w = weight['weight']
                return w
        return None

    def getDerErrorPerOutBetweenTwoNeuron(self, nId1, nId2):
        id1 = min(nId1, nId2)
        id2 = max(nId1, nId2)
        for weight in self.weights:
            if (weight['id1'] == id1 and weight['id2'] == id2):
                return weight['derErrorPerOut']
        return None

    def setWeightBetweenTwoNeuron(self, nId1, nId2, newWeight):
        id1 = min(nId1, nId2)
        id2 = max(nId1, nId2)
        for weight in self.weights:
            if (weight['id1'] == id1 and weight['id2'] == id2):
                weight['weight'] = newWeight
                return

    def setDerErrorPerOutBetweenTwoNeuron(self, nId1, nId2, newDerErrorPerOut):
        id1 = min(nId1, nId2)
        id2 = max(nId1, nId2)
        for weight in self.weights:
            if (weight['id1'] == id1 and weight['id2'] == id2):
                weight['derErrorPerOut'] = newDerErrorPerOut
                return

    # endregion

    # region 9. Prints

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
    def __init__(self, id, value=0, name=""):
        self.id = id
        self.value = value
        self.name = name
        self.derErrorPerOut = None

    # endregion

    # region 2. Getters and Setters

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def getDerErrorPerOut(self):
        return self.derErrorPerOut

    def setId(self, newId):
        self.id = newId

    def setValue(self, newValue):
        self.value = newValue

    def setName(self, newName):
        self.name = newName

    def setDerErrorPerOut(self, newDerErrorPerOut):
        self.derErrorPerOut = newDerErrorPerOut
    # endregion

def main():
    numberOfLayers = 3
    layersSize = [2, 2, 2]
    biases = [0, 0.35, 0.60]
    neuralNetwork = NeuralNetwork(numberOfLayers, layersSize, biases)
    neuralNetwork.creatNeuralNetwork()
    neuralNetwork.creatingWeights()
    neuralNetwork.addingWeights()
    neuralNetwork.addingOutputNeuronsName(["false", "true"])
    neuralNetwork.addingInput([0.05, 0.1], "true")      
    neuralNetwork.calculatingValuesOfNeurons()
    neuralNetwork.backPropagation()


main()
