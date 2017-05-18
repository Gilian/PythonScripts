spam = ['apples', 'bananas', 'tofu', 'cats']

# Function with list as argument
# @return string seperated by comma and the last item with an "and"

def seperateList(pList):
    for i in range(len(pList)):
        if i != (len(pList)-1):
            print(pList[i] + ', ')
        else:
            print('and ' + pList[i])

seperateList(spam)
