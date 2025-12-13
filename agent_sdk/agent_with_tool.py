from dotenv import load_dotenv
from agents import Agent, Runner
from agents import WebSearchTool


load_dotenv()


#  Define an agent
hello_agent = Agent(
    name= "Hello world Agent",
    instructions= "you are an agent which greets the user and helps them ans using emojis and in funny way",
    tools = [
        WebSearchTool()
    ]
)

result = Runner.run_sync(hello_agent,"Hey there, My name is Tejas")
print(result.final_output)