import shelve

# Like a dictionary
shelfFile = shelve.open('mydata')
cats = ['mini', 'timi', 'jimmy']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()