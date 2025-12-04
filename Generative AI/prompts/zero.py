##### ZERO shot Prompting ##########
from openai import OpenAI
from google import genai

client = OpenAI(
    api_key= "AIzaSyDcg1U31nCMOJmbp8oKtJdcfqvwcQOYumc",
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ZERO shot Prompting: Directly giving instructions to model
SYSTEM_PROMPT = "You should only and only ans the coding related questions. " \
"Do not ans anything else.Your name is Alexa. If user ask something other than coding, " \
"just say sorry sir forgive me i can't answer that."
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : "Hey, can u translate hello to spanish language"}
    ]
)

print(response.choices[0].message.content)