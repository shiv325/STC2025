import os
from google import genai

client = genai.Client(api_key = "API_KEY")
chat = client.chats.create(model = "gemini-2.5-flash")

menu = "=" * 60 + " Gemini 2.5 Flash " + "=" * 60

task = '''
Objective => 
    Simulate a job interview. You will:
        a) Collect user information (skills, experience, job position)
        b) Generate up to 10 relevant interview questions
        c) Collect user answers
        d) Provide a rating (out of 10 and a short performance summary

Assignment Instructions =>
    1. Collect Candidate Information :
        Ask the user for ->
            a) Skills/technologies they know
            b) Years of experience
            c) Desired job position
    2. Generate Interview Questions :
        Create 10 interview questions based on the candidate's profile.
    3. Simulate Interview :
        a) Present each question to the user (up to 10)
        b) Collect and store the user's answer for each question.
    4.  Rate and Summarize Performance :
        a) Rate the candidate out of 10.
        b) Provide a summary of their performance.

Do not provide any example walkthrough or unnecessary information. Only present the information that is enough for the user.
Do not provide me any code. You will behave as the interviewer itself.
Ask only question at a time. Do not flood the user with too many questions at once.
Thank the interviewer only at the end of the interview. Do not spam thank you after each response
'''
print(menu)
response = chat.send_message(task)
print(f"Interviewer => {response.text}")

while True :
    request = input("You => ")
    if request == "" :
        choice = input("Do you want to quit? (y/n) => ")
        if choice == "y" :
            input("Press Enter to Quit...")
            os.system("cls")
            break
    else :
        response = chat.send_message(request)
        print(f"Interviewer => {response.text}")
