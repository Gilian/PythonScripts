# Display an inventory
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            # the dic has an item which is the same
            inventory[addedItems[i]] += 1
        else:
            # the dic does not have such an item
            inventory.setdefault(addedItems[i], 1)
    return inventory
    
def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

#displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)


    
