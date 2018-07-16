#coding=utf-8
from math import log
import operator

#给定数据集的香农熵
def calcShannonEnt(dataSet):
    numEntris = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntris #label出现概率
        shannonEnt -= prob * log(prob,2)
    return shannonEnt #香农熵越大,混合的数据种类越多

def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet,labels

#使用第axis个特征划分数据集
def  splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1 #above data has 2 features
    baseEntropy = calcShannonEnt(dataSet) #原始香农熵
    bestInfoGain = 0.
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList) #创建唯一的分类标签列表,above is set([0,1])

        newEntropy = 0.
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            print i,subDataSet
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)

        infoGain = baseEntropy - newEntropy
        print i, u'熵', newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    print u'第',bestFeature,u'个特征是最好的划分数据集特征'
    return bestFeature

#返回出现次数最多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    
def main():
    myMat, labels = createDataSet()
    chooseBestFeatureToSplit(myMat)

main()
