def stringsRearrangement(a):
    for i in range(0,len(a)-1):
        l = len([j for j in range(0,len(a[i])) if a[i][j] != a[i+1][j]])
        if l > 1 or l == 0:
            b = False
            break
    else:
        b = True


    a = sorted(a)

    for i in range(0,len(a)-1):
        l = len([j for j in range(0,len(a[i])) if a[i][j] != a[i+1][j]])
        if l > 1 or l == 0:
            c = False
            break
    else:
        c = True

    print(str(b) + str(c))
    return b or c