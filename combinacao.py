q = 4 
n = 100
p = [0 for i in range(0, q)]
count = 0
def combinacao(np, t):
    global count
    for i in range(t,n+1):
        p[np-1] = i
        if np == q:
            print(p)
            count += 1
            if count == 100:
                exit()
        else:
            combinacao(np+1, t+1)

combinacao(1, 1)
