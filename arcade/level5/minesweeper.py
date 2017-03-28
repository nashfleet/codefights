def minesweeper(m):
    a = pad(m)
    b = []
    s = 0
    for i in range(1, len(a)-1):
        for j in range(1, (len(a[0])-1)):
            s = 0
            s += int(a[i-1][j-1]) + int(a[i-1][j]) + int(a[i-1][j+1])
            s += int(a[i+1][j-1]) + int(a[i+1][j]) + int(a[i+1][j+1])
            s += int(a[i][j-1]) + int(a[i][j+1])
            if j-1 != 0:
                b[i-1].append(s)
            else:    
                b.append([s])
    return b            
        
def pad(m):
    y = len(m)
    x = len(m[0])
    a=[]
    
    for i in range(0, y+2):
        if i == 0 or i == (y+1):
            a.append([0]*(x+2))
        else:
            a.append([0] + m[i-1] + [0])
    return a