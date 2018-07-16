#coding=utf-8
from numpy import *
import matplotlib.pyplot as plt
import knn

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOflines = len(arrayOLines)
    returnMat = zeros((numberOflines ,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+= 1
    return returnMat,classLabelVector

#准备数据(normalize data)
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

def main():
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
    plt.xlabel('video game time')
    plt.ylabel('ice cream sum')
    plt.axis([-2, 25, -.2, 2.])
    plt.show()

#测试算法
def datingClassTest():
    hoRatio = .1
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0] # 值为1000行
    numTestVecs = int(m*hoRatio) #取前100行为测试数据
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = knn.classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "line is %d,classifier came back with: %d,the real answer is %d" % (
            i,classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): errorCount += 1.
    print "total error rate is : %f" % (errorCount/float(numTestVecs))

def classifiPerson():
    resultList = [u'完全不会',u'小概率',u'大概率']
    percentTats = float(raw_input("percent of time spent playing video game?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([percentTats, ffMiles, iceCream])
    classifierResult = knn.classify0([inArr - minVals]/ranges, normMat, datingLabels,3)
    print "you will propabably like this persion: ", resultList[classifierResult-1]
main()
datingClassTest()
classifiPerson()