import random

#This is a guess the number game
randomNumber = random.randrange(1,21)
print("I am thinking of a number between 1 and 20")
guess = 0
guesslimit = 0
guessCounter = 1
while randomNumber != guess and guesslimit < 6:
    try:
        guess = int(input("Take a guess"))
        guesslimit += 1
        print("It is yours ",guessCounter, "/6")
        guessCounter += 1
    except ValueError or TypeError or guess > 20 or guess < 0:
        print("Enter a number between 1-20")
        continue

    if guess < randomNumber:
        print("guess too low")

    elif guess > randomNumber:
        print("guess to high")

    elif guess == randomNumber:
        print("Good job it was ", randomNumber)
        break



if guess == randomNumber:
    print("you won")
else:
    print("you lost")
