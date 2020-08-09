#Function adds looted items to inventory

def addToInventory(inventory, itemsLooted):

    for i in range(len(itemsLooted)):

        if itemsLooted[i] in inventory:
            inventory[itemsLooted[i]] += 1

        else:
            inventory.setdefault(itemsLooted[i], 1)

    return inventory

#Function displays inventory

def displayInventory(inventory):
    total_item = 0

    for k,v in inventory.items():
        print(k,v)
        total_item += v

    return inventory, total_item


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)