from google import genai

client = genai.Client(api_key="AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")

poemTopic = input("Enter the Poem Title => ")

response1 = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = f"Write a Poem on the topic {poemTopic}"
)

generatedPoem = response1.text

print(f"Gemini =>\n{generatedPoem}\n")

decision = input("Wanna modify the poem? (y/n) => ")
if (decision == "y") :
    print("1. Shoten the Poem")
    print("2. Expand the poem with more detail and imagery")
    print("3. Rewrite the poem in a different style")
    print("4. Change the tone of the poem (e.g., joyful, somber, formal, humorous)")

    choice = int(input("Choose the desired option => "))
    additionalInfo = input("Enter any additional details for modification =>\n")
    request = f"{generatedPoem}\n\n"

    if choice == 1 :
        request += "Shorten the Poem"
    elif choice == 2 :
        request += "Expand the poem with more detail and imagery"
    elif choice == 3 :
        request += "Rewrite the poem in a different style"
    elif choice == 4 :
        request += "Change the tone of the poem (e.g., joyful, somber, formal, humorous)"
    
    request += f"\n\n{additionalInfo}"

    response2 = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = request
    )

    modifiedPoem = response2.text

    print(f"Gemini =>\n{modifiedPoem}")
