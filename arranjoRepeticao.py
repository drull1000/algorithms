q = 3
n = 100
count = 0
p = [-1 for i in range(0, q)]
def arranjo(np):
    global count
    for i in range(1,n+1):
        p[np-1] = i
        if np == q:
            print(p)
            count += 1
            if count == 100:
                exit()
        else:
            arranjo(np+1)
arranjo(1)
