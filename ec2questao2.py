n = int(input("Qual a quantidade de vezes que o padrão se repete? "))
message = input("Qual a sua mensagem? ")
code = input("Qual o código? ")

if 0 > n > 10000:
    print("Padrão grande demais. O limite é 10000")
    exit()
if 0 > len(message) > 10000:
    print("Mensagem grande demais. O limite é 10000")
    exit()
if 0 > len(code) > 1000:
    print("Código grande demais. O limite é 1000")
    exit()

def generateTable(message, code):
    table = [-1 for i in range(len(message))]
    for i in range(len(code)):
        for j in range(len(message)):
            if code[i] == message[j]:
                table[j] = i
    table = list(filter((-1).__ne__, table))
    return table
table = generateTable(message, code)

def verifyMessage(n, table):
    i = 0
    while i < len(table)-1:
        if table[i+1] <= table[i]:
            table.pop(i+1)
            n -= 1
            i = 0
        i+=1
    if (n == 0): return 1
    else: return 0

if (verifyMessage(n-1,table)): print("Y")
else: print("N")
