# Program sprawdza czy podany numer telefonu jest poprawnie zbudowany
# Zaklada ze nr sklada sie z 9 cyfr i po kazdych 3 cyfrach jest odseparowany za pomoca "-"

def isPhoneNumber(text):
    if len(text) != 11:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != "-":
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != "-":
        return False

    for i in range(8,11):
        if not text[i].isdecimal():
            return False

    return True

print(isPhoneNumber('444-444-444'))

