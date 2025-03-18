from sklearn import svm
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt


class SupportVectorMachine:
    trainingSamples = []
    trainingLabels = []
    testingSamples = []
    testingLabels = []
    classifier = svm.SVC(kernel='rbf', probability=True)

    def __init__(self, X, Y, x, y):
        self.trainingSamples = X
        self.trainingLabels = Y
        self.testingSamples = x
        self.testingLabels = y

    def predictLabels(self, testSamples):
        return self.classifier.predict(testSamples)

    def model(self):
        model = self.classifier.fit(self.trainingSamples, self.trainingLabels)
        probs = model.predict_proba(self.testingSamples)
        probs = probs[:, 1]

        auc = roc_auc_score(self.testingLabels, probs)
        print('SVM: ROC AUC=%.3f' % auc)

        fpr, tpr, _ = roc_curve(self.testingLabels, probs)
        return fpr, tpr


