#Program check is there is phone number in given message,, if there is it prints it

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False


    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    #Below one is crucial cuz it slices the text of message into 12 characters moving forward with each i incrementation
    chunk = message[i:i + 12]

    #Then if we found phoneNumber using function we print
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
