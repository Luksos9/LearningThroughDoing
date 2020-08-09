def addtoinventory(inventory,lootlist):

    for i in range(len(lootlist)):
        if lootlist[i] in inventory:
            inventory[lootlist[i]] = inventory[lootlist[i]] + 1
        else:
            inventory.setdefault(lootlist[i],1)
    return inventory


def displayInvetory(inv):
    item_total = 0

    for k,v in inv.items():
        print(k,v)
        item_total += v

    print("Total number of items: " + str(item_total))

    return item_total






inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addtoinventory(inv, dragonLoot)
displayInvetory(inv)