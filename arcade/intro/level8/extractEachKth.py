def extractEachKth(i, k):
    del i[k - 1::k]
    return i
