#no memoization used.
valores = [1,5,10,25,50,100]
troco = 1000
tipos = len(valores)

def moedas(tipos, troco):
    if (troco < 0 or tipos == 0): return 0
    elif(troco == 0): return 1
    else:
        return(moedas(tipos,troco-valores[tipos-1])+moedas(tipos-1,troco))
print(moedas(tipos, troco))