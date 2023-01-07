# Prova do algoritmo disponível no final do arquivo.

numeroDeComprimidos = 124
frascos = [1, 5, 10, 25]

def NumeroMinDeFrascos(numeroDeComprimidos, frascos):
    frascosUsados = 0
    while numeroDeComprimidos > 0:
        maiorFrasco = max(frascos)
        if numeroDeComprimidos - maiorFrasco >= 0: 
            frascosUsados += 1
            numeroDeComprimidos -= maiorFrasco
        else:
            frascos.remove(maiorFrasco)
    return frascosUsados

print(f"Podemos usar no mínimo {NumeroMinDeFrascos(numeroDeComprimidos, frascos)} frascos.")

"""
Prova global do algoritmo:

Recebemos um número inteiro representando o número de comprimidos que precisam ser armazenados, e uma lista de números inteiros representando os tamanhos das garrafas que estão disponíveis. Precisamos encontrar o número mínimo de garrafas necessárias para armazenar todos os comprimidos.

Caso base:

Se n = 0, então nenhum comprimido precisa ser armazenado. O algoritmo retorna corretamente 0 garrafas.

Caso indutivo:

Suponha que o algoritmo esteja correto para todos os valores de n' < n de comprimidos. Precisamos mostrar que ele também está correto para n.

Em cada etapa do algoritmo, a maior garrafa disponível é escolhida para armazenar o maior número possível de remédios. Isto significa que o algoritmo está sempre fazendo uma escolha local ótima. Como o algoritmo termina quando todos os comprimidos foram armazenados, constatamos que ele também fará uma escolha globalmente ótima.

Portanto, por indução, o algoritmo é globalmente correto para todos os valores de n.
"""


