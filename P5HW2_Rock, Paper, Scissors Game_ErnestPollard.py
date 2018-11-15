#Rock Paper Scissors
#11/11/2018
#CTI-110 P5HW2-Rock, Paper, Scissors Shoot!
#Ernest Pollard

import random

#create generator for computer choices
def generateRandomNumber():
    randomNumber = random.randint(1, 3)
    return randomNumber

def getComputerChoice(randomNumber):
    if randomNumber == 1:
        computerChoice = "rock"
    elif randomNumber == 2:
        computerChoice = "paper"
    elif randomNumber == 3:
        computerChoice = "scissors"

    return computerChoice

#create user input options
def getUserChoice():
    userChoice = input("Please enter your choice: ")
    return userChoice

#creating/ determinnig winner messages
def determineWinner(computerChoice, userChoice):
    rockMessage = "The rock smashes the scissors"
    scissorsMessage = "The scissors cuts paper"
    paperMessage = "Paper covers rock"
    winner = "no winner"
    message = ""

#how the game is played   
    if computerChoice == "rock" and userChoice == "scissors":
        winner = "Computer"
        message = rockMessage
    elif computerChoice == "scissors" and userChoice == "rock":
        winner = "User"
        message = rockMessage

    if computerChoice == "scissors" and userChoice == "paper":
        winner = "Computer"
        message = scissorMessage
    elif computerChoice == "paper" and userChoice == "scissors":
        winner = "User"
        message = scissorMessage

    if computerChoice == "paper" and userChoice == "rock":
        winner = "Computer"
        message = paperMessage
    elif computerChoice == "rock" and userChoice == "paper":
        winner = "User"
        message = paperMessage

    return winner, message

#If there is no winner
def newGame():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print()
    print("Computer's choice", computerChoice)
    winner, message = determineWinner( computerChoice, userChoice)

    if winner != "no winner":
        print(winner, "won(", message, ")")

    return winner 

#outcome of initial game
def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print()
    print( "Computer's choice", computerChoice )
    winner, message = determineWinner(computerChoice, userChoice)

    if winner != "no winner":
        print(winner, "won(", message, ")")

    while winner == "no winner":
            print("\nMade the same choice")
            winner =  newGame()
            
main()
