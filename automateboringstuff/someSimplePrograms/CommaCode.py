#Function takes an item from list and prints one after another with comma and space + and before last item

spam = ['apples', 'bananas', 'tofu', 'cats']

def PrintWithComas(spam):

    stored = ""
    for number in range(1, len(spam)):

        stored += spam[number-1] + ", "

        if number == len(spam)-1:

            stored = stored + "and " + spam[number]




    print(stored)

PrintWithComas(spam)