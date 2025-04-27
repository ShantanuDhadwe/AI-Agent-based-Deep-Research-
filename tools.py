from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END, START
from main import research_agent, answer_drafting_agent

workflow = StateGraph(dict)

workflow.add_node("research_agent", research_agent)
workflow.add_node("answer_drafting_agent", answer_drafting_agent)


workflow.add_edge(START, "research_agent")
workflow.add_edge("research_agent", "answer_drafting_agent")
workflow.add_edge("answer_drafting_agent", END)

graph = workflow.compile()

initial_state = {
    "query": "What are the latest advancements GPU from NVIDIA?"
}
final_state = graph.invoke(initial_state)

print("Final Answer:")
print(final_state["answer"])
