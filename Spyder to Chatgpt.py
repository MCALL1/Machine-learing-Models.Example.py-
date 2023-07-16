# This script was writen with Spider 3.10 IDE
import openai

# Set up OpenAI API credentials
openai.api_key = 'add your API key'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        temperature=1,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Main script
print("Welcome to Mike's Chatbot your wish is my command :p")

while True:
    user_input = input("Please type your prompt--> ")

    if user_input.lower() in ['exit', 'quit']:
        break

    # Interact with ChatGPT
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)




