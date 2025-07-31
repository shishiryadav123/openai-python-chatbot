import os
import openai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Load API key
openai.api_key = os.getenv("OPENAI_API_KEY")

print("🤖 ChatGPT CLI — Type 'exit' to quit\n")

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4", "gpt-4o" if your key supports it
            messages=[
                {"role": "system", "content": "You're a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response['choices'][0]['message']['content']
        print(f"🤖 ChatGPT: {reply}\n")

    except Exception as e:
        print("❌ Error:", e)
