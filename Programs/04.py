import random
import os

os.system("cls")
while True :
    print("=" * 10 + " Number Guessing Game " + "=" * 10)
    generatedNum = random.randint(1, 10)
    print("Generated Random Number between 1 & 10...")
    userGuess = int(input("Guess a Number [1 - 10] => "))
    if userGuess == generatedNum :
        print("Correct Guess")
        choice = input("Do you want to Play Game Again (y/n) => ")
        if (choice == "n") :
            input("Press Enter to Exit the Game...")
            os.system("cls")
            break
    else :
        input("Incorrect Guess. Press Enter to Try Again...")
    os.system("cls")