def consecutiveBit(n):
    a = str(bin(n))[2:]
    for i in range(0,len(a)-1):
        if int(a[i]) & int(a[i+1]):
            return 1
    return 0