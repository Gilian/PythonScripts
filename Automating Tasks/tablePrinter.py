# Prints a well defined table

# vars
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

# @param: List of Strings, @return: Organized table with right aligned columns
def printTable(tableData):
    colWidths = [0] * len(tableData) # Number of lists
    for i in range(len(colWidths)):
        colWidths[i] = tableData[i]
        print(colWidths[i])

printTable(tableData)
