message = "oi eu sou o drull"
code = ["e", "s", "d"]
# we can create an array with the 
# indexes of the message and wether the
# code until that part is present or not.
table = [[0 for i in range(len(message))] for j in range(len(code))]
# 0 for false, 1 for true

def verifyMessage(message, code, n, messageLength):
    for i in range(len(code)):
        for c in range(len(message)):
            if code[i] == message[c]:
                table[i][c] = 1
    print(table)

verifyMessage(message, code, 1, len(message))