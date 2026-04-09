def planner_agent(state):
    question = state["question"]

    return {
        "plan": f"Find capital city of country in: {question}"
    }