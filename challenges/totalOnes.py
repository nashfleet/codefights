def totalOnes(k):
    s = 0
    for i in range(k+1):
        s += bin(i)[2:].count("1")
    return s
