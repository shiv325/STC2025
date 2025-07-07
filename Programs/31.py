import os
from google import genai

client = genai.Client(api_key="AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")

menu = "=" * 15 + " Gemini 2.5 Flash " + "=" * 15

while True :
    print(menu)
    request = input("You => ")
    if request == "" :
        choice = input("Do you want to quit? (y/n) => ")
        if choice == "y" :
            input("Press Enter to Quit...")
            os.system("cls")
            break

    finalResponse = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = request
    )

    print(f"Gemini => {finalResponse.text}")