def collatz(number):
    if number % 2 == 0:
        evenNumber = number//2
        print(evenNumber)
        return evenNumber

    elif number % 2 == 1:
        oddNumber = 3* number +1
        print(oddNumber)
        return oddNumber
while True:
    try:
        userType = int(input("Wpisz liczbe:"))

    except ValueError and TypeError:
        print("Blad. Podaj liczbe!")


    if collatz(userType) == 1:
        break