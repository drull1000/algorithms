array = [1,5,3,6,78,4,2,9,55,100,22,8]
def maxmin(esquerda,direita):
    if esquerda == direita:
        return array[esquerda], array[direita]
    elif esquerda == (direita+1):
        if array[esquerda] < array[direita]:
            return array[esquerda], array[direita]
        else:
            return array[direita], array[esquerda]
    else:
        meio = (esquerda+direita)//2
        a1, b1 = maxmin(esquerda, meio)
        a2, b2 = maxmin(meio+1, direita)
        return min(a1,a2), max(b1,b2)
print(maxmin(0,10))