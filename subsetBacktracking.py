n = 5
V = [0 for i in range(0, n+1)]
S = [0 for i in range(0, n+1)]
def GeraSub (ns, t):
    for i in range(t,n+1):
        S[ns-1]= V[i]
        count = 0
        for j in range(0, len(S)):
            count += S[j]
        if count % 2 != 0:
            print(S)
        if(i<n):
            GeraSub (ns+1, i + 1)

for i in range(1,n+1):
    V[i] = int(input("Digite um numero: "))

GeraSub (1, 1)

