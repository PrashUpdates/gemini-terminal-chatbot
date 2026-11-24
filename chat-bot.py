from google import genai
from google.genai import errors
import time

# Gemini API Client
client = genai.Client(
    api_key="YOUR_API_KEY"
)

# Create Chat
chat = client.chats.create(
    model="gemini-3.5-flash"
)

print("================================")
print("       GEMINI AI CHATBOT")
print("================================")
print("Type 'exit' to close the chatbot.")
print("--------------------------------")

while True:
    try:
        user = input("\nYou: ")

        if user.lower().strip() == "exit":
            print("\nBot: Goodbye!")
            break

        if not user.strip():
            continue

        reply = chat.send_message(user)

        print("\nBot:", reply.text)

    except errors.ServerError as e:
        print("\nBot: Gemini server is currently busy.")
        print("Please try again after some time.")

    except errors.ClientError as e:
        print("\nBot: API request error.")
        print("Error:", e)

    except KeyboardInterrupt:
        print("\n\nBot: Chatbot stopped.")
        break

    except Exception as e:
        print("\nBot: Something went wrong.")
        print("Error:", e)