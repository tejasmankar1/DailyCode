###########few shot Prompting wwith output serialization #############
from openai import OpenAI
from google import genai

client = OpenAI(
    api_key= "YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You should only ans coding related questions. do not ans anything else. youur name is alexa. 
if user asks something other than coding just say sorry.

Rules:
-Strictly follow the output in JSON format

Output format:
{{
    "code" : "string" or null,
    "isCodingQuestion" : boolean
}}
Examples: 
Q:hey can u explain the trignometry concept?
A: {{
    "code" : null,
    "isCodingQuestion" : False
}}

Q:hey write a code for adding to numbers in python?
A: {{
    "code" : "def add(a,b):
                return a + b" ,
    "isCodingQuestion" : True
}} 
def add(a,b):
        return a + b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user" , "content" : "hey can u give me code to print hello world"}
    ]
)
print(response.choices[0].message.content)