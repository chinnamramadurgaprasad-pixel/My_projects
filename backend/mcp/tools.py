def mock_search(query: str):
    data = {
        "india": "New Delhi is the capital of India.",
        "france": "Paris is the capital of France.",
        "germany": "Berlin is the capital of Germany.",
        "italy": "Rome is the capital of Italy.",
        "spain": "Madrid is the capital of Spain.",
        "usa": "Washington, D.C. is the capital of the USA.",
        "japan": "Tokyo is the capital of Japan.",
        "china": "Beijing is the capital of China.",
        "australia": "Canberra is the capital of Australia.",
    }

    for key in data:
        if key in query.lower():
            return data[key]

    return "No data found"