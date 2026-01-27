📊 Financial Agent (Polygon + LangGraph)

A tool-using financial data agent built with LangGraph, Gradio, and Polygon APIs.
The system demonstrates how to build a traceable, non-hallucinating AI agent that retrieves real market data via external tools instead of relying on model memory.

🚀 Key Features

Tool-using AI agent (ReAct pattern)

LangGraph state machine for deterministic control flow

Polygon API integration (quotes, aggregates, news, financials)

Gradio UI for interactive testing

Full tool & message trace (debuggable and interview-friendly)

Fail-fast config & credential validation

Production-style project structure

🧠 Why This Project Exists

Most LLM demos hallucinate financial data.

This project explicitly prevents hallucination by:

Forcing the agent to call external tools

Showing every tool call and response

Surfacing API errors transparently

This is critical for finance, analytics, and enterprise systems.

🏗️ Architecture Overview
User (Gradio UI)
   ↓
LangGraph Agent (ReAct)
   ↓ decides tool call
Polygon Tool (API)
   ↓ returns real data or error
LangGraph Agent
   ↓
Final Answer + Trace

Core Design Principles

Agent ≠ Chatbot → Agent is a state machine

No silent failures

Observability by default

Separation of concerns

📂 Project Structure
FinanceAgent/
├── src/finagent/
│   ├── config.py        # Env loading & validation
│   ├── llm.py           # OpenAI client creation
│   ├── logging.py       # Structured logging
│   ├── tools/
│   │   └── polygon_tools.py
│   ├── agent/
│   │   ├── graph.py     # LangGraph state machine
│   │   ├── state.py     # Agent state schema
│   │   ├── runner.py   # Execution wrapper
│   │   └── guardrails.py
│   └── ui/
│       └── gradio_app.py
├── .env.example
├── pyproject.toml
└── README.md

🧩 Technologies Used

Python 3.10+

LangGraph – agent orchestration

LangChain Core – message abstractions

OpenAI API – reasoning engine

Polygon.io API – financial data

Gradio – UI layer

🔐 Environment Setup

Create a .env file in the project root:

OPENAI_API_KEY=sk-REAL_KEY_HERE
POLYGON_API_KEY=REAL_POLYGON_KEY
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0
LOG_LEVEL=INFO


⚠️ Never commit .env files to version control.

▶️ Running the Application
1. Create & activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

2. Install dependencies
pip install -e .

3. Start the UI
python -m finagent.ui.gradio_app

4. Open in browser
http://127.0.0.1:7860

🧪 How to Test (Recommended Queries)
Latest Quote
What is the latest quote for AAPL?

Time-range Aggregates
What has been ABNB's daily closing price between March 7, 2024 and March 14, 2024?

News
Summarize the latest news for TSLA.

Error Handling
What is the latest quote for XYZABC?

🔍 Tool / Message Trace

The UI includes a collapsible trace panel that shows:

Human messages

Agent decisions

Tool calls

Tool responses

Final answers

This makes the system auditable and debuggable.

⚠️ Polygon API Limitations (Important)

Polygon enforces data entitlements by subscription tier.

On the free plan, many endpoints return:

NOT_AUTHORIZED – Please upgrade your plan