import gradio as gr
from langchain_core.messages import BaseMessage

from ..config import get_settings
from ..logging import setup_logging
from ..llm import make_llm
from ..tools import make_polygon_tools
from ..agent import build_graph
from ..agent.runner import run_query


def format_trace(messages: list[BaseMessage]) -> str:
    if not messages:
        return "_No trace available._"

    parts = []
    for i, m in enumerate(messages, start=1):
        role = m.__class__.__name__.replace("Message", "")
        parts.append(f"### {i}. {role}")

        content = getattr(m, "content", "")
        if content:
            parts.append(f"```text\n{content}\n```")

        tool_calls = getattr(m, "tool_calls", None) or getattr(m, "additional_kwargs", {}).get("tool_calls")
        if tool_calls:
            parts.append("**Tool calls:**")
            parts.append(f"```json\n{tool_calls}\n```")

    return "\n\n".join(parts)


def main():
    settings = get_settings()
    setup_logging(settings)

    llm = make_llm(settings)
    tools = make_polygon_tools(settings)
    chain = build_graph(llm, tools)

    def financial_agent(input_text: str):
        result = run_query(chain, input_text)
        return result["output"], format_trace(result["trace"])

    with gr.Blocks(title="Financial Agent (Polygon + LangGraph)") as demo:
        gr.Markdown("# Financial Agent (Polygon + LangGraph)")
        gr.Markdown("Ask about quotes, aggregates, news, or financials. Open trace to show tool calls.")

        inp = gr.Textbox(lines=2, placeholder="Ask about quotes, aggregates, news, financials...")
        out = gr.Markdown(label="Answer")

        with gr.Accordion("Tool / Message Trace (Interview Demo)", open=False):
            trace_md = gr.Markdown()

        gr.Button("Run").click(financial_agent, inputs=inp, outputs=[out, trace_md])

    demo.launch(
    server_name="127.0.0.1",
    server_port=7860,
    share=True,          # ✅ creates a public link
    show_error=True
)



if __name__ == "__main__":
    main()
