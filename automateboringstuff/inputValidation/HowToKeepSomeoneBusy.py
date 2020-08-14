"""Program does following:
   1.Ask the user if they’d like to know how to keep an idiot busy for hours.
   2.If the user answers no, quit.
   3.If the user answers yes, go to Step 1."""

userInput = None

while userInput != "no":
    userInput = input("Want to know how to keep an idiot busy for hours?\n").lower()

print("Thank you have a nice day")

"""Same program using pyinputplus module (it has many other useful functions for inputs)"""

import pyinputplus as pyip

while True:
    response = pyip.inputYesNo("Want to know how to keep an idiot busy for hours?\n")
    if response == "no":
        break

print("Have a nice day")