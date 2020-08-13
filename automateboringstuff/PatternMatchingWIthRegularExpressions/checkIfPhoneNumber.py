# Program check if the telephone number is correct
# It assumes that the phone number is made of 9 digits separated by dash "-"
"""using Regex module is much more efficient in this type of programs"""

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


userNumber = input("Enter your phone number (e.g 444-444-444)\n")

if isPhoneNumber(userNumber):
    print("Your number:", userNumber, "is a phone number")

else:
    print("Your number isn't a phone number")