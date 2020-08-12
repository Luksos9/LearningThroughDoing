#Below there are shown 3 ways to create function that checks whether password is strong or not

from re import compile, search

REGEX = compile(r'\d+[^0-9a-zA-Z]*[A-Z]+[^0-9a-zA-Z]*[a-z]+')


def is_strong_password(password):
    return len(password) >= 8 and bool(search(REGEX, ''.join(sorted(password))))



from re import compile

UP_REGEX = compile(r'[A-Z]')
LOW_REGEX = compile(r'[a-z]')
DIG_REGEX = compile(r'\d')


def check_password(text):
    return bool(UP_REGEX.search(text) and LOW_REGEX.search(text) and
                DIG_REGEX.search(text))


assert check_password('kenIsgreat99') is True

import re

def strongPassword(password):
    if passRegex1.search(password) == None:
        return False
    if passRegex2.search(password) == None:
        return False
    if passRegex3.search(password) == None:
        return False
    if passRegex4.search(password) == None:
        return False
    else:
        return True

passRegex1 = re.compile(r'\w{8,}')
passRegex2 = re.compile(r'\d+')
passRegex3 = re.compile(r'[a-z]')
passRegex4 = re.compile(r'[A-Z]')

if strongPassword('Thishasatleast8characters') == True:
    print("Strong Password")
else:
    print("This is not a strong password")