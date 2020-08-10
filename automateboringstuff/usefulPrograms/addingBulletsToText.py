#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points (* ) to the start
# of each line of text on the clipboard.

"""So program when you copy text (ctrl + c) and then run it, returns text with '* ' added to each line"""
import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)

print(text)