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

def generateArray(message, code):
    array = [-1 for i in range(len(message))]
    for i in range(len(code)):
        for j in range(len(message)):
            if code[i] == message[j]:
                array[j] = i
    array = list(filter((-1).__ne__, array))
    return array
array = generateArray(message, code)

def verifyMessage(n, array):
    i = 0
    while i < len(array)-1:
        if array[i+1] <= array[i]:
            array.pop(i+1)
            n -= 1
            i = 0
        i+=1
    if (n == 0): return 1
    else: return 0

if (verifyMessage(n-1,array)): print("Y")
else: print("N")
