
# This script was writen with Spider 3.10 IDE
# -*- coding: utf-8 -*-
import openai
from googletrans import Translator

# Set up OpenAI API credentials
openai.api_key = 'add your API key'

# Initialize the translator
translator = Translator()

# Current Supported languages
languages = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ru': 'Russian',
    'pt': 'Portuguese',
    'ar': 'Arabic',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    # Add more languages here
}

# Function to translate text
def translate_text(text, target_lang):
    if target_lang != 'en':
        translated = translator.translate(text, dest=target_lang).text
        return translated
    return text

# Function to interact with ChatGPT
def chat_with_gpt(prompt, target_lang):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None
    )
    translated_response = translate_text(response.choices[0].text.strip(), target_lang)
    return translated_response

# Main script
print("Welcome to Mike's translator:")

# Get target language from the user
print("Please select the target language you want returned:")
for lang_code, lang_name in languages.items():
    print(f"{lang_code}: {lang_name}")

target_lang = input("Enter the target language code: ")
while target_lang not in languages:
    print("Unsupported language. Please try again.")
    target_lang = input("Enter the target language code: ")

print(f"Translating to {languages[target_lang]}...")

while True:
    user_input = input("Please type your prompt (in English): ")

    if user_input.lower() in ['exit', 'quit']:
        break

    # Interact with ChatGPT
    response = chat_with_gpt(user_input, target_lang)

    print(f"{languages[target_lang]}: {response}")

    change_lang = input("Do you want to change the target language code? (y/n): ")
    if change_lang.lower() == 'y':
        print("Available target languages:")
        for lang_code, lang_name in languages.items():
            print(f"{lang_code}: {lang_name}")

        target_lang = input("Enter the target language code: ")
        while target_lang not in languages:
            print("Unsupported language. Please try again.")
            target_lang = input("Enter the target language code: ")

        print(f"Translating to {languages[target_lang]}...")

    exit_prompt = input("Type 'exit' or 'quit' to end the translation program: ")
    if exit_prompt.lower() in ['exit', 'quit']:
        break
