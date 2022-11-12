m = 13
odd = False
if m % 2 != 0:
    odd = True
    m+=1
t = [[0] * (m+1) for i in range(0,m+1)]

def torneio(m):
    if m == 2:
        t[1][1] = 1
        t[1][2] = 2
        t[2][1] = 2
        t[2][2] = 1
    elif m % 2 != 0:
        torneio(m+1)
    else:
        p = m//2
        torneio(p)
        if m % 2 == 0:
            t[p][p] = p
        else:
            t[p][p] = p+1

        for i in range(1,p+1):
            for j in range(1,p+1):
                t[i+p][j] = t[i][j]+p
                t[i][j+p] = m-(j-i+m) % p
                t[m-(j-i+m) % p][j+p] = i
torneio(m)

if odd:
    for c in range(m):
        for i in range(m):
            if t[c][i] == (m):
                t[c][i] = "bye"
        print(t[c])
else: 
    for c in range(m+1):
        print(t[c])