import os

qna = {
    "how are you" : "I'm well.",
    "what is your name" : "I am ChatBot.ai.",
    "describe yourself" : "I am a Static ChatBot.",
    "what can you do" : "I can respond to some of your requests",
    "tell me current location" : "CGC Landran, Mohali."
}

print("=" * 15 + " ChatBot " + "=" * 15)

while (True) :
    ques = input("You => ").lower()
    if ques == "" :
        choice = input("Wanna quit conversation (y/n) => ")
        if (choice == "y") :
            input("Press Enter to Quit...")
            os.system("cls")
            break
    else :
        print("ChatBot.ai => ", end = "")
        if (ques not in qna) :
            print("Wrong Question...")
        else :
            print(qna[ques])