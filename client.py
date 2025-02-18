from openai import OpenAI
import requests
import re
import privkey as keys
from time import sleep as wait
print("Checking keys, initializing models...")
client= OpenAI(api_key=keys.OPENAI_API_KEY)
print("Welcome to Feather\n\nUsing GPT4o-mini")
wait(2)
print('Ringing the AI service...')
completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that excels in answering questions."},
            {
                "role": "user",
                "content": f"123 Testing.. testing testing testing..."
            }
        ]
    )
print("AI service is ready.")
wait(0.5)
response=""
print("You're connected! Say hi to the AI!")
while True:

    proompt = input("> ")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "assistant",
                "content": response
            },
            {"role": "user", "content": "You are a helpful assistant that excels in answering questions."},
            {
                "role": "user",
                "content": proompt
            }
        ]
    )
    print(str(completion.choices[0].message.content))
    response=str(completion.choices[0].message.content)