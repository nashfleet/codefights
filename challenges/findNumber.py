def findNumber(n):
    if n==0:
        return 0
    x=3*n
    return int(str(x-2)+str(x-1)+str(x))
