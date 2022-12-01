valores = [1,5,10,25,50,100]
troco = 1000
tipos = len(valores)
memo = [[-1 for i in range(0, 10000)] for c in range(0,10000)]

def moedas(tipos, troco):
    if (troco < 0 or tipos == 0): return 0
    elif(troco == 0): return 1
    else:
        if memo[tipos][troco] == -1:
            memo[tipos][troco] = (moedas(tipos,troco-valores[tipos-1])+moedas(tipos-1,troco))
        return memo[tipos][troco]

print(moedas(tipos, troco))