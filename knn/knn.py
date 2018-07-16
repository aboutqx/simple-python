#coding=utf-8
from numpy import *
import operator
import matplotlib.pyplot as plt

def createDataSet():
    group = array([
        [1.,1.1], 
        [1.,1.], 
        [0,0], 
        [0,.1]])
    labels = ['A', 'A' ,'B', 'B']
    return group, labels

#labels 代表已知数据的特征值,在这里是分类值
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances**.5

    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse = True)

    return sortedClassCount[0][0]

def main():
    group, labels = createDataSet()
    test = array([2., 1.])
    print 'class:',classify0(test, group, labels, 3)

    for i in range(4):
        plt.text(group[i][0], group[i][1],labels[i])
        plt.plot(group[i][0], group[i][1], 'bo')
    plt.text(test[0], test[1], 'test')
    plt.plot(test[0], test[1], 'bo')
    plt.axis([-.2, 2.2, -.2, 2.2])
    plt.show()


if __name__ == '__main__':
    main()

