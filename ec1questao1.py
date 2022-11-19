array = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]

def repeated(array, currentElement, count, auxCount, repeatedElement):
    if currentElement+1 == len(array): 
        return repeatedElement
    else:
        if array[currentElement] == array[currentElement + 1]: 
            if auxCount > count: 
                repeatedElement = array[currentElement]
                return repeated(array, currentElement+1, auxCount, auxCount+1, repeatedElement)
            else: 
                return repeated(array, currentElement+1, count, auxCount+1, repeatedElement)
        else:
            return repeated(array, currentElement+1, count, auxCount, repeatedElement)

print(repeated(array, 0, 0, 0, 0))