from typing import TypedDict

class AgentState(TypedDict):
    question: str
    plan: str
    answer: str