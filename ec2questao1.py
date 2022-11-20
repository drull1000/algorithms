#Dado um conjunto S de 1 <= n <= 20 inteiros e um inteiro positivo x. Proponha e implemente um algoritmo que verifica se existe um subconjunto de S cuja soma de seus elementos seja x.
s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 10
t = [ [-1] * 500 for i in range(500) ]
def soma(p,n):
    if p == 0 or n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if t[p][n] == -1:
            t[p][n] = soma(p-1, n-s[p-1])+soma(p-1,n)
        return t[p][n]
print(soma(20,7))
for c in range(21):
    print(t[c])