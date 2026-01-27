# Financial Agent (Polygon + LangGraph)

A tool-using financial agent that answers questions using Polygon market data tools.
Includes:
- LangGraph agent loop (tool calls until final answer)
- Gradio UI with collapsible tool trace
- FastAPI endpoints (/ask, /trace, /health)
- Basic tests

## Setup

### 1) Create environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
