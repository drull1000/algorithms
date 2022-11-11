array = ["V","V","V","V","V","V","V","V","V","F","F","F","F","F"]
#array = ["V","V","V","V","V","V","V","V","V"]

def countFalse(array, currentElement, count):
    if currentElement == len(array):
        return 0 
    elif array[currentElement] == "F":
        return len(array)-count
    else:
        if array[currentElement] != "F": #Elemento atual é igual a "V" 
            return countFalse(array, currentElement+1, count+1)

print(countFalse(array, 0, 0))