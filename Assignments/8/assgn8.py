import os
from google import genai

client = genai.Client(api_key = "API_KEY")
chat = client.chats.create(model = "gemini-2.5-flash")

menu = "=" * 60 + " Gemini 2.5 Flash " + "=" * 60

task = '''
Objective => 
    Create an interactive, Gemini-powered mystery or puzzle game where the AI acts as the game master—generating clues, tracking the game state, and responding dynamically to user actions.
    The game should blend storytelling, logic, and data-driven challenges, making use of Python and relevant libraries.


Assignment Tasks =>
    1. Game Setup :
        a) Let the user choose a game theme or genre (e.g., detective mystery, science quest, historical adventure)
        b) The AI (Gemini) introduces the story and sets the first scene.
    2. Multi-Mode Gameplay :
        Implement at least two of the following modes:
        a) Clue Generation: Gemini generates clues or riddles based on the story and user's progress.
        b) Quiz Challenges: At key points, the AI asks data-driven or subject-based questions (e.g., math puzzles, logic problems, or even questions using real datasets with NumPy/Pandas).
        c) Code Puzzle Mode: For a programming-themed game, Gemini can generate code snippets with bugs for the player to debug, or mini coding challenges to solve.
        d) Visualization Mode: Present data-based clues using plots made with characters and symbols (e.g., “Analyze this chart to deduce the next locationˮ).
    3. Dynamic Storytelling and Prompt Engineering :
        a) Use prompt engineering to have Gemini adapt the story, clues, and responses based on user input and game state.
        b) Allow the player to use commands like /clue, /quiz, /solve, or /hint to interact with the game master.
    4.  Game State & Progress Tracking :
        a) Track the user's progress, inventory (if applicable), and score.
        b) Optionally, save and load game sessions.
    5. Streaming Output Enhancement :
        a) As Gemini narrates or gives clues, animate the output to mimic real-time storytelling.

Start by asking the user the id and password, and then proceed further in the way that you are told.
If the id is not found, give the option to create one. Display the username all the time.
After logging in, ask the user to choose game genre and then continue with the saved progress in that theme.
Do not provide any example walkthrough or unnecessary information. Only present the information that is enough for the user.
Do not provide me any code. You will behave as the game itself.
All the games should be of easy level and very simple to understand.
'''
print(menu)
response = chat.send_message(task)
print(f"Mr. Puzzle => {response.text}")

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
        print(f"Mr. Puzzle => {response.text}")
