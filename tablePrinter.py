# Prints a well defined table

# vars
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'], #1
    ['Alice', 'Bob', 'Carol', 'David'], #2
    ['dogs', 'cats', 'moose', 'goose']] #3

# @param: List of Strings, @return: Organized table with right aligned columns
def printTable(tableData):
    colWidths = [0] * len(tableData) # Number of lists (here: 3)
    longest = 0

    # Calculate the longest word in any list
    for i in range(len(colWidths)):
        colWidths[i] = tableData[i]
        for j in range(len(colWidths[i])): # Lenght of all items
            # Calculates the longest word
            if longest < len(colWidths[i][j]):
                longest = len(colWidths[i][j])
                
    # Iterate over the list to display items          
    for x in range(len(tableData)):
        if x > 0:
            print('\n')
        for y in range(len(tableData[i])):
            #addSpaces = longest - len(tableData[x][y])
            print((tableData[x][y]).rjust(longest+1), end='')

    
printTable(tableData)
