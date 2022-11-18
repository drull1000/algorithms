def buscaTernaria(array, inicio, fim, alvo):
    if fim >= inicio:
        meio1 = (inicio + fim) // 3

        if meio1 > 3:
            meio2 = meio1 * 2

            if array[meio1] == alvo:
                return meio1

            elif array[meio2] == alvo:
                return meio2
                
            elif array[meio2] < alvo:
                return buscaTernaria(array, meio2 + 1, fim, alvo)
                
            elif array[meio1] < alvo and array[meio2] > alvo:
                return buscaTernaria(array, meio1+1, meio2-1, alvo)
    
            elif array[meio1] > alvo:
                return buscaTernaria(array, inicio, meio1 - 1, alvo)
   
        else:
            meio1 = (inicio+fim)
 
        if array[meio1] == alvo:
            return meio1
 
        elif array[meio1] > alvo:
            return buscaTernaria(array, inicio, meio1 - 1, alvo)

        elif array[meio1] < alvo:
            return buscaTernaria(array, meio1+1, fim, alvo)
 
    else:
        return -1
 
array = [2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 4
 
resultado = buscaTernaria(array, 0, len(array)-1, alvo)
 
if resultado != -1:
    print("Elemento no index", str(resultado))
else:
    print("O elemento não existe!")