# agents.py

def guard_agent(state):
    user = state.get("user")
    if not user:
        raise Exception("Unauthorized")

    if user["role"] not in ["admin", "manager"]:
        raise Exception("Access denied")

    return state

def query_agent(state):
    q = state["question"].lower()

    if "employee" in q or "salary" in q:
        state["route"] = "sql"
    elif "report" in q or "policy" in q:
        state["route"] = "vector"
    else:
        state["route"] = "llm"

    return state
