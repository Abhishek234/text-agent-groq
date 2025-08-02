#!/usr/bin/env python3
"""
Multi-Task Text Agent using Groq LLMs
"""

import os
import sys
import openai
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Configure Groq API
openai.api_base = "https://api.groq.com/openai/v1"
openai.api_key = os.getenv("GROQ_API_KEY")

def choose_task() -> str:
    print("📋 Choose a task:")
    print("1. Summarize")
    print("2. Rewrite")
    print("3. Compose Email")
    print("4. Change Tone")
    choice = input("Enter number: ").strip()
    tasks = {
        "1": "summarize",
        "2": "rewrite",
        "3": "compose",
        "4": "change tone"
    }
    return tasks.get(choice, "summarize")

def get_email_input() -> str:
    print("\n✍️ Enter your text below (press Ctrl+D or Ctrl+Z when finished):")
    print("-" * 50)
    try:
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
        content = '\n'.join(lines)
        if not content.strip():
            print("❌ No input provided.")
            sys.exit(1)
        return content
    except KeyboardInterrupt:
        print("\n❌ Cancelled.")
        sys.exit(1)

def main():
    task = choose_task()
    user_input = get_email_input()

    # Prompt routing
    if task == "summarize":
        system_prompt = "Summarize the following in 2–3 sentences."
    elif task == "rewrite":
        system_prompt = "Rewrite the text to improve clarity and professionalism."
    elif task == "compose":
        system_prompt = "Write a polite, professional email based on the following prompt."
    elif task == "change tone":
        system_prompt = "Change the tone of the text to be more friendly and casual."
    else:
        system_prompt = "Act as a helpful assistant."

    try:
        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",  # Use a currently supported Groq model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
            temperature=0.3
        )

        print("\n✅ Result:\n")
        print(response['choices'][0]['message']['content'])

    except Exception as e:
        print(f"❌ Error: {e}")
        print("This might be due to:")
        print("- Invalid API key")
        print("- Model not available on Groq")
        print("- Network connectivity issues")
        sys.exit(1)

if __name__ == "__main__":
    main()