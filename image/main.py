from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI()


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        { "role" : "user", "content" : [
            {"type" : "text", "text" : "generate a caption for this image in about 20 words."},
            {"type" : "image_url", "image_url" : ""}
        ]}
    ]
)

print(response.choices[0].message.content)