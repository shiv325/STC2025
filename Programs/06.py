import os

os.system("cls")
while (True) :
    print("=" * 15 + " Calculator " + "=" * 15)
    res = input("Enter Expression (Empty to Exit) => ")
    if (res == "") :
        choice = input("Do you want to Exit (y/n) => ")
        if (choice == "y") :
            input("Press Enter to Exit...")
            os.system("cls")
            break
    else :
        print(f"Result => {eval(res)}")
        input("Press Enter to Restart...")
    os.system("cls")