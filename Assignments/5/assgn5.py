import google.generativeai as genai

genai.configure(api_key="API_KEY")

equation = input("Enter Math Problem => ")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    f"Solve the math problem step-by-step :\n{equation}\nUse fractions in form a/b if needed"
)

print(f"Gemini =>\n{response.text}\n")
