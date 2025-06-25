import os
from google import genai

client = genai.Client(api_key = "API_KEY")
chat = client.chats.create(model = "gemini-2.5-flash")

menu = "=" * 60 + " Gemini 2.5 Flash " + "=" * 60

task = '''
Objective => 
    Enhance the existing Gemini chat app to create a “Smart Study Buddyˮ that helps students with a variety of academic tasks, making use of Gemini's generative and streaming capabilities.

Assignment Tasks =>
    1. Subject-Aware Chatbot :
        a) Allow the user to select a subject at the start (e.g., Math, History, Computer Science).
        b) The bot should tailor its responses and explanations to the selected subject.
    2. Multi-Mode Assistance :
        Implement at least two of the following modes:
        a) Q&A Mode: Answer factual questions or explain concepts.
        b) Quiz Mode: Generate quiz questions and check user answers.
        c) Summary Mode: Summarize long text provided by the user (e.g., lecture notes).
        d) Code Helper Mode: For programming subjects, generate and explain code snippets.
    3. Enhanced User Interface
        a) Display the conversation history in a readable format.
        b) Clearly label user and Gemini responses.
        c) Optionally, add simple commands (e.g., /summary, /quiz, /explain) to switch modes.
    4. Streaming Output Enhancement
        a) As Gemini streams its answer, display a loading indicator or animate the output to mimic real-time typing.
    5. (Bonus) Save & Review Sessions
        a) Allow users to save their chat session to a file.
        b) Implement a command to review past sessions.

Start by asking the user the subject and then proceed further in the way that you are told.
Do not provide any example walkthrough or unnecessary information. Only present the information that is enough for the user.
'''
print(menu)
response = chat.send_message(task)
print(f"Smart Study Buddy => {response.text}")

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
        print(f"Smart Study Buddy => {response.text}")
