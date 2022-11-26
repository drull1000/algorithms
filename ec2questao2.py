checks = []
def verifyMessage(n, message, code):
    table = [-1 for i in range(len(message))]
    #loop through the entire message to find it. write a check on the index
    # mark where the code chars are
    # loop back going from where they are, ignoring the index with check
    # until the next char.
    if n == 0:
        return 1
    for i in range(len(code)):
        for j in range(len(message)):
            #create array with code indexes and where they appear
            if code[i] == message[j]:
                #table[j] = i
                table[j] = i
    #remove all the -1's from the array
    table = list(filter((-1).__ne__, table))

    #----------------------------
    # WE ALREADY HAVE THE ARRAY, WE JUST NEED TO SEE IF THE VALUE IS GOING TO 
    # DECREASE AND CHANGE THE VALUE OF OUR N AS IT DOES.
    #----------------------------

    for i in range(len(table)-1): 
        # if the current item is lesser than the next one
        # and different from -1
        #we need to check if the current item is always increasing

        #if table[i] < table[i+1] and (table[i] != -1 and table[i+1] != -1):
        if table[i+1] != -1:
            if table[i] < table[i+1]:
                pass
            #the pattern is met if the last item we saw is equal to the legth of the code
            print(table[i])
            if table[i] == len(code):
                print("pattern met")

    
    print("---")
    print(table)
    print("---")
    print(checks)

verifyMessage(2, "eu sou drull", "esdl")

# look for first code in the string.
# call 