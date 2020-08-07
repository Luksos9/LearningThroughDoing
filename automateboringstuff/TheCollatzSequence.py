#The program checks if the number is Even or Odd, does certain calculations/
#based on that and ends when function returns value == 1

def collatz(number):
    #sprawdz czy liczba jest parzysta, wykonaj dzialanie, zwroc wartosc
    if number % 2 == 0:
        evenNumber = number//2
        print(evenNumber)
        return evenNumber

    #sprawdz czy jest nieparzysta
    elif number % 2 == 1:
        oddNumber = 3* number +1
        print(oddNumber)
        return oddNumber

#main loop, ends when returned value of function collatz() is equal to 1
while True:
    try:
        userType = int(input("Wpisz liczbe:"))

    except ValueError and TypeError:
        print("Error! Please Enter a number that is INTEGER")


    if collatz(userType) == 1:
        break