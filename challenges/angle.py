def angle(a):
    b = 0
    for i in str(a):
        i = int(i)
        if i==8 or i==5:
            b += 2
        elif i==4:
            b += 6
        elif i==0:
            continue
        else:
            b += 1
    return b