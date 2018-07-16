def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readLines():
        lineArr = line.strip().split()
        dataMat.append([1, 0, ])