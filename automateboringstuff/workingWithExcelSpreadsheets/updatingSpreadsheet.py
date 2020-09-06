"""This program updates cells in a spreadsheet of produce sales.
program will look through the spreadsheet, find specific kinds of produce, and update their prices.

Program does the following:

1.Loops over all the rows
2.If the row is for garlic, celery, or lemons, changes the price"""

#! python3
# updateProduce.py - Corrects costs in produce sales spreadsheet.

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

# The produce types and their updated prices
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}

# TODO: Loop through the rows and update the prices.