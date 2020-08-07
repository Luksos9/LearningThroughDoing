import random

#Rock, Paper, Scissors Game

tie = 0
win = 0
loose = 0
userMove = ""
while userMove != "q": #Main loop, breaks when user chooses quit
    print("{} wins, {} losses, {} Ties".format(win, loose, tie))
    userMove = input("Enter your move:\n"
                                      "(r) - rock\n"
                                      "(p) - paper\n"
                                      "(s) - scissors\n"
                                      "(q) - quit\n")
    if userMove not in ("p,r,s,q"):
        print("Wrong!")
        print("Enter your move: (r) - rock\n"
                                      "(p) - paper\n"
                                      "(s) - scissors\n"
                                      "(q) - quit\n")
    a = ["p", "r", "s"]
    computerMove = random.choice(a)

    if computerMove == userMove:
        print("{} vs {}. It is a Tie!".format(computerMove, userMove))
        tie += 1
    elif computerMove == "p" and userMove == "r":
        print("{} vs {}. Computer wins!".format(computerMove, userMove))
        loose += 1
    elif computerMove == "r" and userMove == "p":
        print("{} vs {}. Player wins!".format(computerMove, userMove))
        win += 1
    elif computerMove == "s" and userMove == "p":
        print("{} vs {}. Computer wins!".format(computerMove, userMove))
        loose += 1
    elif computerMove == "p" and userMove == "s":
        print("{} vs {}. Player wins!".format(computerMove, userMove))
        win += 1
    elif computerMove == "r" and userMove == "s":
        print("{} vs {}. Computer wins!".format(computerMove, userMove))
        loose += 1
    elif computerMove == "s" and userMove == "r":
        print("{} vs {}. Player wins!".format(computerMove, userMove))
        win += 1
    elif userMove == "q":
        print("Bye!")
        break