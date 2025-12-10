from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional,Literal
from langgraph.graph import StateGraph,START,END
from openai import OpenAI

load_dotenv()

client = OpenAI()

class State(TypedDict):
    user_query : str
    llm_output = Optional[str]
    is_good = Optional[bool]

def chatbot(state: State):
    print("Chatbot node",state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role" : "user", "content" : state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state : State) -> Literal["chatbot_gemini","endnode"]:
    print("evaluate_respone Node",state)
    evaluation = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role" : "system", "content" : "You are a strict evaluator. Return only 'yes' or 'no'."},
            {"role" : "user", "content" : f"Is the following response correct?\n\nUser Query: {state['user_query']}\nAssistant Answer: {state['llm_output']}"}
        ]
    ).choices[0].message.content

    if "yes" in evaluation:
        state["is_good"] = True
        return "endnode"
    else:
        state["is_good"] = False
        return "chatbot_gemini"

def chatbot_gemini(state: State):
    print("cahtbot_geminni Node", state)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role" : "user", "content" : state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state : State):
    print("Endnode",endnode)
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode",endnode)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_conditional_edges("chatbot","evaluate_response")
graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode",END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query" : "Hey what is 2+2?"}))
print(updated_state)