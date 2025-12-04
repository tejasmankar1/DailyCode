######Persona based Prompting
from openai import OpenAI
from dotenv import load_dotenv
from google import genai
load_dotenv()

client = OpenAI(api_key="YOUR_API_KEY",
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Tejas.
    You are acting on behalf of Tejas who is 23 years old Tech enthusiatic and 
    engineer. Your main tech stack is Data Science and Python and You are learning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : "hey who are u"}
    ]
)

print(response.choices[0].message.content)