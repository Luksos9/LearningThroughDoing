# This program can replace the text on the clipboard with just the phone numbers and email addresses it finds.
# Useful if you want the boring task of finding every phone number and email adress in a long doc or web page.
""" To run this program just go to some web page or doc press ctrl + A to select all the text
    Then just press ctrl + c to copy it to clipboard. When you run this program it will give u emails and phone nums"""
import pyperclip
import re

# Creat Phone Number regex

phoneRegex = re.compile(r"""(   #r used to read 'raw' text, so as it is
(\d{3}|\(\d{3}\))?              #the area of code
(\s|-|\.)?                      #separator " " or - or .
(\d{3})                         #first 3 digits
(\s|-|\.)                       #separator
(\d{4})                         #last 4 digit
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #optional extension
)""", re.VERBOSE)

# Create Email regex

emailRegex = re.compile(r"""(
[a-zA-Z0-9._%+-]+   #username
@                   #@ symbol
[a-zA-Z0-9.-]+      #name of domain
(\.[a-zA-Z]{2,4})   #dot and after it something (.pl or .com etc)
)""", re.VERBOSE)    #VERBOSE allows you to add whitespace and comments

# Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
