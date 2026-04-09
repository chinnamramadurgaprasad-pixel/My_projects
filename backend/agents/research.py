from mcp.tools import mock_search  

def research_agent(state):
    question = state["question"]

    # Call tool
    result = mock_search(question)

    return {
        "answer": result
    }