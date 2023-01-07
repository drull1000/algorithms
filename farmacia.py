numeroDeComprimidos = 123
frascos = [1, 5, 10, 25]

def NumeroMinDeFrascos(numeroDeComprimidos, frascos):
    frascosUsados = 0
    while numeroDeComprimidos > 0:
        maiorFrasco = max(frascos)
        if numeroDeComprimidos - maiorFrasco >= 0: 
            print(f'Capacidade do frasco usado: {maiorFrasco}')
            frascosUsados+=1
            numeroDeComprimidos = numeroDeComprimidos - maiorFrasco
        else:
            frascos.remove(maiorFrasco)
    return frascosUsados

print(f"O número mínimo de fracos que podemos usar é {NumeroMinDeFrascos(numeroDeComprimidos, frascos)}")

