#this is a simple rock paper scsisors program
import random
compChoice = random.randint(1, 3)
exitCode = 0
userScore=0
compScore=0
userString = "null"
while exitCode < 2:
    compChoice = random.randint(1, 3)
    userChoice = int(input("Pick your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
    if userChoice == 1:
        userString = "Rock"
    if userChoice == 2:
        userString = "Paper"
    if userChoice == 3:
        userString = "Scissors"

    if compChoice == 1:
        compString = "Rock"
    if compChoice == 2:
        compString = "Paper"
    if compChoice == 3:
        compString = "Scissors"

    print(f"You chose {userString} \n The computer chose {compString}")
    if userChoice == compChoice:
        print("The result is a tie!")

    if userChoice == 1 and compChoice == 2:
        print("You lose!")
        compScore = compScore + 1
    if userChoice == 2 and compChoice == 3:
        print("You lose!")
        compScore = compScore + 1
    if userChoice == 3 and compChoice == 1:
        print("You lose!")
        compScore = compScore + 1
    if userChoice == 1 and compChoice == 3:
        print("You win!")
        userScore = userScore + 1
    if userChoice == 2 and compChoice == 1:
        print("You win!")
        userScore = userScore + 1
    if userChoice == 3 and compChoice == 2:
        print("You win!")
        userScore = userScore + 1
    exitCode=int(input(f"The computer has won {compScore} times \n You have won {userScore} times \n Press 1 to continue or press 2 to exit: "))
print("Thank you for playing \n created by Charles King \n 08/12/2026")
