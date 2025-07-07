import random
import os

options = ("Exit", "Rock", "Paper", "Scissors")
outcomes = ("CPU Wins!", "You Win!", "Tie!")
os.system("cls")
while (True) :
    print("=" * 7 + " Rock Paper Scissors Game " + "=" * 7)
    cpuChoice = random.randint(1, 3)
    print("Your Options => ")
    for i in range(4) :
        print(f"{i}. {options[i]}")
    option = int(input("Select Your Option (0 - 3) => "))
    if (option == 0) :
        choice = input("Do you want to Exit (y/n) => ")
        if (choice == "y") :
            input("Press Enter to Exit...")
            os.system("cls")
            break
        os.system("cls")
        continue
    print(f"Your Choice => {options[option]}")
    print(f"CPU Choice => {options[cpuChoice]}")
    if (option == cpuChoice) :
        print(outcomes[2])
    elif (option == 1) :
        if (cpuChoice == 2) :
            print(outcomes[0])
        else :
            print(outcomes[1])
    elif (option == 2) :
        if (cpuChoice == 3) :
            print(outcomes[0])
        else :
            print(outcomes[1])
    else :
        if (cpuChoice == 1) :
            print(outcomes[0])
        else :
            print(outcomes[1])
    input("Press Enter to Continue...")
    os.system("cls")