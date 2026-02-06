# graph.py
from langgraph.graph import StateGraph, END
from agents import guard_agent, query_agent
from tools import (
    search_vector_db,
    llm_generate,
    text_to_sql,
    run_sql
)

import os
DB_URL = os.getenv("DB_URL")

def vector_path(state):
    res = search_vector_db(state["question"])
    context = res["documents"][0][0]
    state["answer"] = llm_generate(context)
    return state

def llm_path(state):
    state["answer"] = llm_generate(state["question"])
    return state

def sql_path(state):
    sql = text_to_sql(state["question"], "employees")
    rows = run_sql(DB_URL, sql)
    if not rows:
        state["answer"] = "No data found in SQL table"
    else:
        state["answer"] = rows
    return state


graph = StateGraph(dict)

graph.add_node("guard", guard_agent)
graph.add_node("query", query_agent)
graph.add_node("vector", vector_path)
graph.add_node("llm", llm_path)
graph.add_node("sql", sql_path)

graph.set_entry_point("guard")
graph.add_edge("guard", "query")

graph.add_conditional_edges(
    "query",
    lambda s: s["route"],
    {
        "vector": "vector",
        "llm": "llm",
        "sql": "sql"
    }
)

graph.add_edge("vector", END)
graph.add_edge("llm", END)
graph.add_edge("sql", END)

agentic_graph = graph.compile()
