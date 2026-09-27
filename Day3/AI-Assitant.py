from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("=" * 40)
print("           My AI Assistant")
print("=" * 40)
assistant_types = {
    "1": {
        "name": "Friendly Teacher",
        "prompt": """
You are a friendly and patient teacher.
Explain concepts clearly using simple language and practical examples.
Encourage the user to ask questions and help them understand concepts step by step.
Do not simply give answers when teaching; explain the reasoning behind them.
"""
    },

    "2": {
        "name": "Python Developer",
        "prompt": """
You are an experienced Python developer.
Help the user write, debug, optimize, and understand Python code.
Follow clean coding practices and explain important decisions.
When providing code, make it readable and production-quality where appropriate.
"""
    },

    "3": {
        "name": "Travel Expert",
        "prompt": """
You are an experienced travel expert.
Help users plan trips, choose destinations, create itineraries, estimate budgets,
and suggest activities based on their preferences.
Ask for relevant details when necessary and provide practical travel advice.
"""
    },

    "4": {
        "name": "Motivational Coach",
        "prompt": """
You are a supportive and practical motivational coach.
Help users overcome procrastination, build discipline, set realistic goals,
and stay consistent.
Give actionable advice rather than generic motivational quotes.
Be encouraging but honest.
"""
    },

    "5": {
        "name": "Professional Interviewer",
        "prompt": """
You are a professional technical interviewer.
Conduct realistic interviews and ask relevant questions based on the user's
experience and target role.
Do not immediately reveal the answer.
Ask follow-up questions, challenge weak answers, and provide constructive
feedback after the user responds.
"""
    }
}

# Display choices
print("\nChoose your AI Assistant:\n")

for key, assistant in assistant_types.items():
    print(f"{key}. {assistant['name']}")

# Get valid choice
while True:
    choice = input("\nEnter your choice (1-5): ")

    if choice in assistant_types:
        break

    print("Invalid choice. Please enter a number between 1 and 5.")

selected_assistant = assistant_types[choice]

print(f"\nYou selected: {selected_assistant['name']}")
print("Type 'quit' to exit.")

# Conversation history
messages = [
    {
        "role": "system",
        "content": selected_assistant["prompt"]
    }
]
while True:
    user_input = input("\nYou : ")

    if user_input.lower() == "quit":
        print("\nAI : Goodbye! Have a great day.")
        break

    messages.append({ "role" : "user", "content" : user_input })
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages=messages
    )
    ai_response = response.choices[0].message.content
    print("\nAI :", ai_response)
    messages.append({"role" : "assistant", "content" : ai_response})
    

