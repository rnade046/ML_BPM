import zipfile
import synapseclient
import re

from tf import TranscriptionFactorBindingSite
from svm import SupportVectorMachine as svm
from lr import LogisticRegression as lr
from roc import ReceiverOpperativeCharacteristics as roc


def importFile():
    """ Download PBM data using synapse client """
    syn = synapseclient.Synapse()
    syn.login('rnade046@uottawa.ca', 'csi5180project')

    # Obtain a pointer and download the data
    syn2898428 = syn.get(entity='syn2898428')

    # Get the path to the local copy of the data file
    training_filePath = syn2898428.path

    return training_filePath


def readDataFile(filePath):
    """ Read data file, obtain PBM sequences and binding affinities associated to their tested transcript factor """
    tfList = []

    # Unzip file and read contents
    with zipfile.ZipFile(filePath, 'r') as zip_ref:
        file_name = re.split('=', str(re.split('\\s+', str(zip_ref.infolist()[0]))[1]))[1].replace("'", "")
        training_file = zip_ref.open(str(file_name))

        for line in training_file:

            lineF = re.split('\t|\n', line.decode("UTF-8"))

            # keep sequences obtained from HK method and that wasn't flagged (0)
            if lineF[1] == 'HK' and int(lineF[9]) == 0:

                if not tfList:
                    tfList.append(TranscriptionFactorBindingSite(lineF[0]))
                    currentTf = 0
                    pass
                else:
                    tfExists = False
                    for i in range(0, len(tfList)):
                        if tfList[i].getName() == lineF[0]:
                            tfExists = True
                            currentTf = i

                    if not tfExists:
                        tfList.append(TranscriptionFactorBindingSite(lineF[0]))
                        currentTf = i + 1

                # calculate affinity as median - background
                affinity = float(lineF[5]) - float(lineF[6])

                # clean sequence (ie. remove last 25 ncl)
                seq = lineF[2][:35]

                # store sequence and affinity
                tfList[currentTf].addSample(seq, affinity)

    totalTF = len(tfList)
    # split data for training
    trainingTF = tfList[0:int(((totalTF*0.8)-1))]
    testingTF = tfList[int((totalTF*0.8)):totalTF]

    return trainingTF, testingTF

def extractTrainingExamples(tfList, length):
    from data import Data

    data = Data()

    for i in range(0, len(tfList)):

        # sort sequences of a given transcription factor in ascending order based on binding affinity
        tf = tfList[i]
        tf.sortSequences()
        tf.sortAffinities()

        for j in range(0, len(tf.sortedSequences)):

            # interested in first 200 and last 200 sequences (negative and positive instances)
            if j < 200 or j > (len(tf.sortedSequences) - 200):

                seq = tf.sortedSequences[j]

                # ENUMERATE MOTIF for given sequence
                for k in range(0, len(seq) - length):
                    motif = seq[k:k + length]
                    if j < 200:
                        data.addNegativeInstance(motif)
                    else:
                        data.addPositiveInstance(motif)

    return data

def encodeOneHot():
    """ Initialize one hot encoding for reproducible encodings """
    from numpy import array
    from sklearn.preprocessing import OneHotEncoder

    alphabet = ['A', 'C', 'G', 'T']
    values = array(alphabet)
    values = values.reshape(len(values), 1)

    encoder = OneHotEncoder()
    encoder.fit(values)

    return encoder


def main():
    # motif length of interest
    motif_length = 10

    # Download and read file
    trainingFile = importFile()
    trainingTF, testingTF = readDataFile(trainingFile)

    # Encode data
    encoder = encodeOneHot()

    training_data = extractTrainingExamples(trainingTF, motif_length)
    training_data.encodeSamples(encoder)
    training_data.generateLabels()

    testing_data = extractTrainingExamples(testingTF, motif_length)
    testing_data.encodeSamples(encoder)
    testing_data.generateLabels()

    # Initialize models
    svm_model = svm(training_data.getSamples(), training_data.getLabels(), testing_data.getSamples(), testing_data.getLabels())
    lr_model = lr(training_data.getSamples(), training_data.getLabels(), testing_data.getSamples(), testing_data.getLabels())

    # Assess performance
    svm_fpr, svm_tpr = svm_model.model()
    lr_fpr, lr_tpr = lr_model.model()

    # Plot ROC for results
    plot = roc([svm_fpr, svm_tpr], [lr_fpr, lr_tpr])
    plot.plotROC()

if __name__ == '__main__':
    main()
