def displayInvetory(invetory):

    print("Your invetory:")
    valueCounter = 0
    for item,value in invetory.items():

        print(item, value)

        valueCounter += value

    print("Total number of items: " + str(valueCounter))

invetory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInvetory(invetory)