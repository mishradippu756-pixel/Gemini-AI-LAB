import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(api_version="v1")
)

question = input("Ask Gemini: ")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=question
)

print("\nGemini:")
print(response.text)