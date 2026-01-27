from langgraph.graph import StateGraph, END
from langgraph.prebuilt import create_react_agent, ToolNode, tools_condition

from .state import AgentState

def build_graph(llm, tools):
    """
    Version-resilient LangGraph agent:
    - create_react_agent decides tool calls
    - ToolNode executes tools
    - tools_condition routes agent -> tools or -> END
    """
    agent = create_react_agent(llm, tools)
    tool_node = ToolNode(tools)

    workflow = StateGraph(AgentState)
    workflow.add_node("agent", agent)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        tools_condition,
        {
            "tools": "tools",
            END: END,
        },
    )

    workflow.add_edge("tools", "agent")
    return workflow.compile()
