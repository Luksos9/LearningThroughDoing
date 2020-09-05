#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook(r'C:\Users\lukas\OneDrive\Pulpit\automateboringStuff\censuspopdata.xlsx')
sheet = wb.active
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

"""What else could be done using such program?
*Compare data across multiple rows in a spreadsheet.
*Open multiple Excel files and compare data between spreadsheets.
*Check whether a spreadsheet has blank rows or invalid data in any cells and alert the user if it does.
*Read data from a spreadsheet and use it as the input for your Python programs."""