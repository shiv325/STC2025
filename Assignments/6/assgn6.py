import os
from google import genai

client = genai.Client(api_key = "AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")
chat = client.chats.create(model = "gemini-2.5-flash")

menu = "=" * 60 + " Gemini 2.5 Flash " + "=" * 60

while True :
    print(menu)
    request = input("You => ")
    if request == "" :
        choice = input("Do you want to quit? (y/n) => ")
        if choice == "y" :
            input("Press Enter to Quit...")
            os.system("cls")
            break
    else :
        response = chat.send_message(request)
        print(f"Gemini => {response.text}")
