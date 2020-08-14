"""Program that asks users for their sandwich preferences.
   Using PyInputPlus as training of that module"""

import pyinputplus as pyip

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], lettered=True)
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], lettered=True)
addCheese = pyip.inputYesNo("Do you want cheese?(Yes/No)")
a = ""
amountOfSandwiches = pyip.inputInt("How many sandwiches do you want?",min=1)

if addCheese.lower() == "yes":
    addCheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt= 'What type of cheese do you want?\n',
                               lettered=True)
else:
    addCheese = "No cheese" #could also be just blank

extrasList = ["mayo", "mustard", "lettuce", "tomato"]
extras = []

for extra in range(len(extrasList)):
    extrasToAdd = pyip.inputYesNo("Do you want {} (Yes/No)".format(extrasList[extra]))
    if extrasToAdd == "yes":
        extras.append(extrasList[extra])

for item in extras:
    a += " {}".format(item)

print("You get {} sandwiches :".format(amountOfSandwiches), breadType, proteinType, addCheese, a)

# TODO: Making this program shorter
# TODO: Adding more comments
# TODO: Adding prices for each of options, and display a total cost.
