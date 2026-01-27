from langchain_core.messages import HumanMessage
from .state import AgentState
from .guardrails import basic_input_guardrails

def run_query(chain, user_input: str) -> dict:
    """
    Returns:
      output: final assistant answer
      trace: full message list (includes tool calls + tool outputs)
    """
    basic_input_guardrails(user_input)

    state: AgentState = {
        "messages": [HumanMessage(content=user_input)]
    }

    result = chain.invoke(state)
    messages = result.get("messages", [])
    final_text = messages[-1].content if messages else ""

    return {"output": final_text, "trace": messages}
