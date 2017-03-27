def removeDigits(n, k):
    a=[]
    for i in range(0,len(str(n))-k+1):
        a.append(int(str(n)[i:i+k]))
    return [min(a), max(a)]