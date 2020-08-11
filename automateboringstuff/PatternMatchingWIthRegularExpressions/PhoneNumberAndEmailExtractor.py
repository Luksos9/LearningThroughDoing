# This program can replace the text on the clipboard with just the phone numbers and email addresses it finds.
# Useful if you want the boring task of finding every phone number and email adress in a long doc or web page.

import pyperclip
import re

phoneRegex = re.compile(r"""(
(\d{3}|\(\d{3}\))?              #the area of code
(\s|-|\.)?                      #separator -
(\d{3})                         #first 3 digits
(\s|-|\.)                       #separator
(\d{4})                         #last 4 digit
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)""", re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.


