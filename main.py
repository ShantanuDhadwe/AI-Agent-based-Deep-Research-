from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END, START
from langchain_tavily import TavilySearch

load_dotenv()
llm = ChatGroq(model = "llama-3.1-8b-instant",temperature= 0)

search_tool = TavilySearch()


def research_agent(state):
    query = state["query"]
    search_results = search_tool.run(query)
    state["research"] = search_results
    return state

def answer_drafting_agent(state):
    research = state["research"]
    drafting_prompt = f"Based on the following research, draft a concise and informative answer:\n\n{research}"
    answer = llm.invoke([HumanMessage(content=drafting_prompt)])
    state["answer"] = answer.content
    return state


 



