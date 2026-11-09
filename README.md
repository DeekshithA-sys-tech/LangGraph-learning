# LangGraph Learning

Hands-on notebooks and a small Ollama-backed agent project for learning LangGraph.

## Contents

- `Hello_World.ipynb` — a basic state graph and greeting node.
- `Muptiple_Input.ipynb` — processing multiple values in one node.
- `Sequential_Agent.ipynb` — passing state through sequential nodes.
- `Conditional_agent.ipynb` — routing to different operations conditionally.
- `Exercise1.ipynb`–`Exercise3.ipynb` — practice exercises for state and nodes.
- `OpenAI-project/` — Python agent examples and pinned dependencies.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r OpenAI-project/requirements.txt
```

The agent in `OpenAI-project/agent.py` uses Ollama. Install and start Ollama,
then download the model it expects:

```powershell
ollama pull deepseek-r1:1.5b
python OpenAI-project/agent.py
```

The notebooks can be opened in Jupyter after installing the dependencies.
