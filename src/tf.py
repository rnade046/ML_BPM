class TranscriptionFactorBindingSite:
    name = ""
    bindingSequences = []
    bindingAffinities = []
    sortedSequences = []
    sortedAffinities = []

    def __init__(self, tfName):
        self.name = tfName

    def addSample(self, seq, aff):
        self.bindingSequences.append(seq)
        self.bindingAffinities.append(aff)

    def sortSequences(self):
        self.sortedSequences = [x for _, x in sorted(zip(self.bindingAffinities, self.bindingSequences))]

    def sortAffinities(self):
        self.sortedAffinities = sorted(self.bindingAffinities)

    def getName(self):
        return self.name

    def getBindingSequences(self):
        return self.bindingSequences

    def getBindingAffinities(self):
        return self.bindingAffinities
