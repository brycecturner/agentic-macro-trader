# Agentic AI Portfolio Manager

A modular, agent-based portfolio management system that leverages CrewAI to coordinate research, risk, and trading agents for automated investment analysis and decision-making.

---

## 🚀 Overview

**Agentic AI Portfolio Manager** is designed to automate the process of researching, analyzing, and making trading decisions for equity portfolios. The system uses multiple specialized AI agents—each with a distinct role—to collaboratively generate actionable insights and trading recommendations. All agent activities and system events are logged for transparency and future analysis.

---

## 🏗️ Architecture

- **Language:** Python 3.11
- **AI Framework:** [CrewAI](https://github.com/joaomdmoura/crewAI)
- **Data Access:** [yfinance](https://github.com/ranaroussi/yfinance), Serper API, web scraping tools
- **Logging:** Python logging module (file-based, logs stored in `/logs`)
- **Environment:** Conda (`environment.yml` provided)

### Directory Structure

```
.
├── agents/           # Agent definitions (research, risk, trader)
├── crew/             # Crew assembly and parallel execution logic
├── logs/             # Log files for each agent and crew
├── tasks/            # Task definitions for each agent
├── tools/            # Utility tools (web search, scraping, price fetch)
├── utils/            # Utility functions (date, output formatting)
├── main.py           # Entry point for running the system
├── research_summary.json # Output: structured research results
├── environment.yml   # Conda environment specification
├── .env              # API keys and environment variables
└── README.md         # Project documentation
```

---

## 🧠 Agents & Roles

| Agent Name                  | Role Description                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| **Research Agents**         | Analyze macroeconomic, sector, and market data to generate actionable insights.                   |
| **Risk Agent** (planned)    | Evaluate portfolio risk metrics (volatility, exposure, drawdown).                                 |
| **Trader Agent**            | Make trading decisions based on research output and live market data.                             |

---

## ⚙️ Features

- **Automated Research:** Multiple research agents analyze macro trends, banking risk, capital flows, fiscal policy, growth, and inflation.
- **Parallel Execution:** Research tasks run concurrently for efficiency.
- **Live Data Integration:** Fetches current stock prices and market data using yfinance and web tools.
- **Structured Output:** Results are saved as structured JSON for downstream use.
- **Logging:** All agent actions and system events are logged to files in `/logs`.
- **Modular Design:** Easily extendable to add new agents, tasks, or tools.

---

## 🏁 Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/agentic-portfolio.git
cd agentic-portfolio
```

### 2. Set Up the Environment

```sh
conda env create -f environment.yml
conda activate project-2
```

### 3. Configure API Keys

- Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY` and `SERPER_API_KEY`.

### 4. Run the System

```sh
python main.py
```

- Research agents will run in parallel.
- Results will be printed to the console and saved to `research_summary.json`.
- Logs will be written to the `/logs` directory.

---

## 📝 Example Output

- **Structured research summaries** in `research_summary.json`
- **Log files** for each agent and crew in `/logs`

---

## 🛠️ Extending the System

- **Add new agents:** Define in `agents/`
- **Add new tasks:** Define in `tasks/`
- **Add new tools:** Place in `tools/` and register with agents as needed

---

## 📚 References

- [CrewAI Documentation](https://docs.crewai.com/)
- [yfinance Documentation](https://github.com/ranaroussi/yfinance)
- [Serper API](https://serper.dev/)

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

Bryce Turner

---

## 💡 Future Work

- Implement Risk Agent for portfolio risk analysis
- Integrate Trader Agent with Interactive Brokers API for live/paper trading
- Add daily portfolio summary reports
- Upgrade logging to PostgreSQL for advanced analytics

---

*For questions or contributions, please open an issue or pull