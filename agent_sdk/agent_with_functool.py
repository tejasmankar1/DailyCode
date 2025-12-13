from dotenv import load_dotenv
from agents import Agent, Runner
from agents import WebSearchTool,function_tool
import requests

load_dotenv()

@function_tool
def get_weather(city: str):
    """
    Fetch the weather for a given city name.
    Args:
        city: The city name to fetch the weather for
    """
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"

#  Define an agent
hello_agent = Agent(
    name= "Hello world Agent",
    instructions= "you are an agent which greets the user and helps them ans using emojis and in funny way",
    tools = [
        WebSearchTool(),
        get_weather
    ]
)

result = Runner.run_sync(hello_agent,"Hey there, My name is Tejas")
print(result.final_output)