class Data:
    pos_instances_seq = []
    neg_instances_seq = []
    samples = []
    labels = []

    def __init__(self):
        self.pos_instances_seq = []
        self.neg_instances_seq = []

    def addPositiveInstance(self, instance):
        self.pos_instances_seq.append(instance)

    def addNegativeInstance(self, instance):
        self.neg_instances_seq.append(instance)

    def getPositiveInstances(self):
        return self.pos_instances_seq

    def getNegativeInstances(self):
        return self.neg_instances_seq

    def getSamples(self):
        return self.samples

    def getLabels(self):
        return self.labels

    def encodeSamples(self, encoder):
        from numpy import array

        for i in range(0, len(self.pos_instances_seq)):
            # one hot encode all instances in training data

            values = array(list(self.pos_instances_seq[i]))
            values = values.reshape(len(values), 1)

            values_encoded = encoder.transform(values)

            self.samples.append(values_encoded.tocsr())

        for i in range(0, len(self.neg_instances_seq)):

            values = array(list(self.neg_instances_seq[i]))
            values = values.reshape(len(values), 1)

            values_encoded = encoder.transform(values)
            self.samples.append(values_encoded.tocsr())



    def generateLabels(self):

        posInstancesSeqs = self.getPositiveInstances()
        negInstancesSeqs = self.getNegativeInstances()

        for i in range(0, len(posInstancesSeqs)):
            self.labels.append(1)

        for i in range(0, len(negInstancesSeqs)):
            self.labels.append(-1)
