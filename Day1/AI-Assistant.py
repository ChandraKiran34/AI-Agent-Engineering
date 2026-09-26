from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("=" * 40)
print("           My AI Assistant")
print("=" * 40)
messages = [
    {
        "role" : "system",
        "content" : "you are a helpful assistant"
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
    

