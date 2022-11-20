#Dado um con = 5njunto S de 1 <= n <= 20 inteiros e um inteiro positivo x. Proponha e implemente um algoritmo que verifica se existe um subconjunto de S cuja soma de seus elementos seja x.
a = [1, 5, 3, 7, 4]
n = 5

#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
arr = [ [-1] * 500 for i in range(500) ]
def somar(a,n,soma):
    if soma == 0:
        return 1
    if n <= 0:
        return 0 
    if arr[n-1] != -1:
        return arr[n-1][soma]
    if a[n-1]>soma:
        arr[n-1][soma] = somar(a, n - 1, soma)
        return arr[n-1][soma]

    else:
        arr[n-1][soma] = somar(a, n - 1, soma)
        return arr[n-1][soma] or somar(a, n-1, soma-a[n-1])
    



print(somar(a,20,13))