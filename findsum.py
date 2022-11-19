#Dado um conjunto S de 1 <= n <= 20 inteiros e um inteiro positivo x. Proponha e implemente um algoritmo que verifica se existe um subconjunto de S cuja soma de seus elementos seja x.
s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 10
a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
t = [ [-1] * 21 for i in range(21) ]
#implement array
def somar(array,n,soma):
    if soma == 0 or n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if t[n-1][soma] != -1:
            return t[n-1][soma]
        if array[n-1] > soma:
            return t[n-1][soma] = somar(array, n-1, soma)
        else:
            return t[n - 1][soma] = somar(array, n - 1, somar) or somar(array, n - 1, soma - t[n - 1]);
    
#print(somar(20,10))

for c in range(21):
    print(t[c])