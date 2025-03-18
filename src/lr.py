from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression

class LogisticRegression:
    trainingSamples = []
    trainingLabels = []
    testingSamples = []
    testingLabels = []
    classifier = LogisticRegression(solver='lbfgs')

    def __init__(self, X, Y, x, y):
        self.trainingSamples = X
        self.trainingLabels = Y
        self.testingSamples = x
        self.testingLabels = y

    def model(self):

        model = self.classifier.fit(self.trainingSamples, self.trainingLabels)
        probs = model.predict_proba(self.testingSamples)
        probs = probs[:, 1]

        auc = roc_auc_score(self.testingLabels, probs)
        print('Logistic: ROC AUC=%.3f' % auc)

        fpr, tpr, _ = roc_curve(self.testingLabels, probs)
        return fpr, tpr

