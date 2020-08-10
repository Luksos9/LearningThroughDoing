#This is much shorter version of checkIfPhoneNumbers programs, using re module that provides finding patterns

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())