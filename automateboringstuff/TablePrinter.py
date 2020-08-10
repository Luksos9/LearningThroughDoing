#!/usr/bin/python3


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    #Create a list with each element representing columns that will store each column max width
    columnWithds = [0] * len(table)

    for list in range(len(table)): #range(len(table)) represents index of list in tableData

        #for every element in each list in table, we comparing their lenghts(they are string) and choosing the biggest
        for element in table[list]:
            if columnWithds[list] < len(element):
                columnWithds[list] = len(element)

    # Print list of lists
    for element in range(len(table[0])):

        for list in range(len(table)):
            print(table[list][element].rjust(columnWithds[list]), end = ' ')
        print()
        element += 1

printTable(tableData)
