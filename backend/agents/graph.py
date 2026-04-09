from langgraph.graph import StateGraph
from .state import AgentState
from .planner import planner_agent
from .research import research_agent

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("planner", planner_agent)
    builder.add_node("research", research_agent)

    builder.set_entry_point("planner")

    builder.add_edge("planner", "research")

    builder.set_finish_point("research")

    return builder.compile()