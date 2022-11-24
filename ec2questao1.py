array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
soma = int(input("Digite a soma desejada: "))
tabela = [[-1 for i in range(soma+1)] for j in range(soma+1)]
subset = [0 for i in range(soma+1)] 
n = len(array)

def acharSoma(array, n, soma):
    if (soma == 0 or soma in array): return 1
    elif (n <= 0 or soma < 0): return 0
    elif (tabela[n - 1][soma] != -1): return tabela[n - 1][soma]
    elif array[n - 1] > soma:
        tabela[n - 1][soma] = acharSoma(array, n - 1, soma)
        return tabela[n - 1][soma]
    else:
        tabela[n - 1][soma] = acharSoma(array, n - 1, soma)
        if (n > subset[soma] and n not in subset): subset[soma] = n
        return tabela[n - 1][soma] or acharSoma(array, n - 1, soma - array[n - 1])

if acharSoma(array, n, soma) == 1:
    count = 0
    printSubset = []
    print(f"Existe um subconjunto para a soma {soma}.")
    for i in range(len(array)-1, -1, -1):
        if array[len(array)-1] != 0 and count+array[i] <= soma:
                count += array[i]
                printSubset.append(array[i])
    print(f"O subconjunto é: {printSubset}")

else:
    print(f"Não existe um subconjunto para a soma {soma}.")