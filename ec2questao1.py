array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
tabela = [[-1 for i in range(100)] for j in range(100)]
subset = [-1 for i in range(100)] 
#soma = int(input("Digite a soma desejada: "))
soma = 50
n = 20

def acharSoma(array, n, soma):
    if soma == 0:
        return 1
    elif n <= 0:
        return 0
    elif tabela[n - 1][soma] != -1:
        return tabela[n - 1][soma]

    elif array[n - 1] > soma:
        tabela[n - 1][soma] = acharSoma(array, n - 1, soma)
        return tabela[n - 1][soma]
    else:
        tabela[n - 1][soma] = acharSoma(array, n - 1, soma)
        # This is interesting. It produces the subset we want, but adds the same number in the sub array.
        if subset[soma] < n and n not in subset:
            subset[soma] = n+1
        print(f"n: {n}")
        print(f"soma: {soma}")
        print(f"--------")
        return tabela[n - 1][soma] or acharSoma(array, n - 1, soma - array[n - 1])
if acharSoma(array, n, soma) == 1:
    print(f"Existe um subconjunto para a soma {soma}")
else:
    print(f"Não existe um subconjunto para a soma {soma}")
print(subset)