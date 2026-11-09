# Simple bot.

# Objectives:

#     1. Define state structure with a list of HumanMessage objects.

#     2. Initialize an Ollama model using LangChain.
#     3. Send and handle messages.
#     4. Build and compile the agent graph.

# Main goal: integrate an LLM in a LangGraph.
from typing import List, TypedDict
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[HumanMessage]


llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0.7)


def process(state: AgentState)-> AgentState:
    response = llm.invoke(state["messages"])
    print(f" \n AI : {response.content}")
    return state

graph = StateGraph(AgentState)

graph.add_node("process", process)

graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

userInput = input("User: ")

while userInput != "quit":
    agent.invoke({"messages": [HumanMessage(content=userInput)]})
    userInput = input("User: ")
