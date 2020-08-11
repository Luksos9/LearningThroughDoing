# This program can replace the text on the clipboard with just the phone numbers and email addresses it finds.
# Useful if you want the boring task of finding every phone number and email adress in a long doc or web page.

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

# TODO: Create email regex.

# Create Email regex

emailRegex = re.compile(r"""(
[a-zA-Z0-9._%+-]+   #username
@                   #@ symbol
[a-zA-Z0-9.-]+      #name of domain
(\.[a-zA-Z]{2,4})   #dot and after it something (.pl or .com etc)
)""", re.VERBOSE)    #VERBOSE allows you to add whitespace and comments

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.


