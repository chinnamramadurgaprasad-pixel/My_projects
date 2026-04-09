def planner_agent(state):
    question = state["question"]

    plan = f"Search and summarize about: {question}"

    return {"plan": plan}