#Dado um conjunto S de 1 <= n <= 20 inteiros e um inteiro positivo x. Proponha e implemente um algoritmo que verifica se existe um subconjunto de S cuja soma de seus elementos seja x.
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
arr = [ [-1] * 500 for i in range(500) ]
def somar(a,n, soma):
    print(n)
    if soma == 0:
        return True
    if n <= 0:
        return False
    if arr[n-1] == -1:
        return arr[n-1][soma]
    if a[n-1]>soma:
        resultado = somar(a, n - 1, soma)
        arr[n-1][soma] = True
    else:
        arr[n-1][soma] = somar(a, n - 1, soma) or somar(a, n - 1, soma - a[n - 1])
        print(f"{arr[n - 1][soma]} resultado")
        return arr[n - 1][soma]
    


print(somar(a,20,13))