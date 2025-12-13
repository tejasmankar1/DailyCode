from dotenv import load_dotenv
from agents import Agent, Runner



load_dotenv()

spanish_agent = Agent(
    name="Spanish Agent",
    instructions= " You translate the users message to spanish"
)


french_agent = Agent(
    name="French Agent",
    instructions= " You translate the users message to french"
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. you use the tools given to you to translate."
        "if asked for multiple translations, you call the relevent tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish"
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French"
        ),
    ]
)

result =  Runner.run_sync(orchestrator_agent,input="Say 'hello, how are you?'in Spanish")
print(result.final_output)
print(result.raw_responses)