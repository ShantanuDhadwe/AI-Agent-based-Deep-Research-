# 🚀 Deep Research AI Agentic System

This project implements a **Deep Research AI System** that crawls websites using **Tavily** for online information gathering. It leverages a **dual-agent architecture** built with **LangGraph** and **LangChain**:

- **Research Agent**: Conducts real-time web research.
- **Answer Drafting Agent**: Crafts concise, informative responses based on gathered information.

> **Important:**
> - `main.py` contains the **agent definitions**.
> - `tools.py` contains the **workflow orchestration and execution code**.

---

# 📁 Project Structure

```
├── main.py    # Defines the research agent and answer drafting agent
├── tools.py   # Builds the LangGraph workflow and runs the system
├── .env       # (Optional) Environment variables (Tavily, Groq API keys)
├── README.md  # Project documentation
```

---

# 🔄 How It Works

### 1. Research Agent (`main.py`)
- Accepts a user query.
- Uses **TavilySearch** to gather up-to-date online information.
- Stores the search results into the system state.

### 2. Answer Drafting Agent (`main.py`)
- Takes the research data.
- Uses **LLama 3.1 8b Instant** (via Groq) to generate a clear, informative answer.

### 3. Workflow Orchestration (`tools.py`)
- Defines a two-node graph (`research_agent` ➔ `answer_drafting_agent`) using **LangGraph**.
- Runs the workflow with a given initial query and outputs the final answer.

---

# 🚪 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd <your-repo-directory>
```

### 2. Install Dependencies

```bash
pip install langchain langgraph langchain_groq langchain_tavily python-dotenv
```

### 3. Set Up Your `.env` File

Create a `.env` file with the following variables:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 4. Run the System

```bash
python tools.py
```

---

# 💬 Example Output

```
Final Answer:
NVIDIA has recently announced several advancements in GPU technology, including the new Blackwell architecture...
```

---

# 🧵 Tech Stack

- **Python**
- **LangChain**
- **LangGraph**
- **Groq API** (LLama 3.1-8b Instant model)
- **Tavily API** (Web search)

---

# 🔧 Implementation Details

### main.py
- **Environment Setup**: Loads environment variables using `dotenv`.
- **LLM Configuration**: Initializes Groq's ChatGroq model with `llama-3.1-8b-instant`.
- **Tool Setup**: Initializes TavilySearch tool.
- **Research Agent**: Accepts a query, runs a web search using Tavily, and stores results.
- **Answer Drafting Agent**: Uses the search results to draft a detailed and informative answer via the LLM.

### tools.py
- **Workflow Building**: Constructs a two-step agentic graph.
- **Node Management**: Adds `research_agent` and `answer_drafting_agent` nodes.
- **Edge Management**: Connects nodes from `START` ➔ `research_agent` ➔ `answer_drafting_agent` ➔ `END`.
- **Execution**: Compiles the graph and runs it with a sample initial query.
- **Output**: Prints the final drafted answer based on online research.

---

# 🌟 Notes

- You can modify the `initial_state` in `tools.py` to customize the input queries.
- The system is easily extensible with additional agents, such as summarization or multi-step analytical agents.

---

