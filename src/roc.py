from matplotlib import pyplot

class ReceiverOpperativeCharacteristics:
    svm_probs = []
    lr_probs = []

    def __init__(self, svm, lr):
        self.svm_probs = svm
        self.lr_probs = lr


    def plotROC(self):
        pyplot.plot(self.svm_probs[0], self.svm_probs[1], color='red', label='SVM')
        pyplot.plot(self.lr_probs[0], self.lr_probs[1], color='blue', label='Logistic')

        pyplot.xlabel('False Positive Rate')
        pyplot.ylabel('True Positive Rate')
        pyplot.legend()

        pyplot.show()
