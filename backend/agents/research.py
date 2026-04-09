def research_agent(state):
    plan = state["plan"]

    # Simulated research
    answer = f"Result based on: {plan}"

    return {"answer": answer}