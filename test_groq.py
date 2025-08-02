import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client with Groq configuration
api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ No API key found! Please set GROQ_API_KEY or OPENAI_API_KEY environment variable.")
    exit(1)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

try:
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Use a currently supported Groq model
        messages=[
            {"role": "system", "content": "Summarize the following in 2–3 sentences."},
            {"role": "user", "content": "Here's a long email about project updates and next week's deliverables. The team has made significant progress on the new feature development, with 75% completion achieved. Marketing materials are being prepared for the upcoming launch, and we need to finalize the budget allocation for Q4 initiatives."}
        ],
        max_tokens=150,
        temperature=0.3
    )

    print("✅ Summary:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"❌ Error: {e}")
    print("This might be due to:")
    print("- Invalid API key")
    print("- Model not available on Groq")
    print("- Network connectivity issues")