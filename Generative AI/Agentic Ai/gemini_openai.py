from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key= "YOUR_API_KEY",
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages=[
        {"role" : "system", "content" : "You are an expert in maths and you have to answer only question related to maths. if the query i snot related to maths just say sorry and do not ans that "},
        {"role" : "user", "content" : "hey can u help me solve a + b whole square"}
    ]
)
print(response.choices[0].message.content)