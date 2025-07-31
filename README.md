# Agentic AI Portfolio Manager - Product Requirements Document (PRD)

## Project Name  
**Agentic AI Portfolio Manager**

---

## Purpose

The purpose of this project is to build an automated, **agent-based portfolio management system** that can analyze equities, generate investment recommendations, manage risk, and optionally execute trades on a paper trading account (e.g., Interactive Brokers). The system uses **CrewAI** to coordinate multiple intelligent agents acting like a research analyst, risk manager, and trader — working together to make portfolio decisions more efficient and scalable.

---

## Core Features

| Agent                | Role Description                                                                                  | MVP Status               |
|----------------------|-------------------------------------------------------------------------------------------------|--------------------------|
| **Research Agent (TechPod)** | Focuses on technology sector stocks (FAANG: AAPL, MSFT, GOOGL, AMZN, META). Analyzes recent developments and trends to generate actionable insights. | Implemented for MVP       |
| **Risk Agent**         | Evaluates portfolio risk metrics such as volatility, exposure, and drawdown to manage potential losses. | Planned for future phases |
| **Trader Agent**       | Places trades based on agent recommendations, interfacing with Interactive Brokers paper trading API. | Planned for future phases |

---

## Architecture

### Tech Stack

| Layer         | Technology                                    |
|---------------|----------------------------------------------|
| AI Framework  | Python + CrewAI                              |
| Data Access   | yfinance, requests, or finnhub API            |
| Trading API   | Interactive Brokers (IB-insync or TWS API)    |
| Logging       | MVP: Rotating log files using Python logging module <br> Future: PostgreSQL logging backend |
| Persistence   | CSV or SQLite (Phase 1)                       |
| Reports       | Text file or CLI printouts                    |

---

## Milestones

| Milestone                              | Description                                                       | ETA         |
|---------------------------------------|-------------------------------------------------------------------|-------------|
| ✅ Environment Setup                   | Conda environment with CrewAI and logging setup                  | Day 1       |
| ✅ Data Access Module                  | Market data fetcher using `yfinance`                              | Day 2       |
| ✅ **TechPod Research Agent MVP**     | Implement single Research Agent focused on technology stocks     | Day 4       |
| ✅ Crew Assembly                      | Wire TechPod agent and task into CrewAI                           | Day 5       |
| ✅ File-Based Logging                 | Implement logging to files for all MVP agent activities          | Day 6       |
| 🟡 Risk Agent Implementation          | Design and develop risk evaluation agent                          | Day 8       |
| 🟡 Trader Agent Integration            | Connect trader agent to Interactive Brokers paper trading API    | Day 9       |
| 🟡 Daily Report Generator              | Generate portfolio summary reports                                | Day 10      |
| 🟡 PostgreSQL Logging (Future)         | Upgrade logging infrastructure to Postgres for queryability      | Post-MVP    |

---

## Requirements

### Functional Requirements

- [x] Implement **TechPod Research Agent** focusing on FAANG technology stocks.
- [ ] Design and implement Risk Agent to calculate portfolio risk metrics.
- [ ] Design and implement Trader Agent to execute trades via Interactive Brokers paper account.
- [ ] CrewAI must coordinate agents and tasks.
- [ ] Market data should be fetched live using `yfinance` or other APIs.
- [x] File-based logging must capture all agent activities and system events.
- [ ] Daily portfolio summary reports must be generated.

### Non-Functional Requirements

- Python 3.10 or 3.11
- Modular codebase for easy agent extension
- Logs stored in `logs/` folder with daily rotation
- Logging format should support future migration to PostgreSQL backend

---

## File Structure (Initial)

agentic-portfolio/
├── agents/
│ ├── research_agent.py #   TechPod Research Agent (MVP)
│ ├── risk_agent.py # Risk evaluation agent (planned)
│ └── trader_agent.py # Trader agent for order execution (planned)
├── tasks/
│ ├── research_tasks.py # Tasks for Research Agent
│ ├── risk_tasks.py # Tasks for Risk Agent (planned)
│ └── trader_tasks.py # Tasks for Trader Agent (planned)
├── crew/
│ └── crew_setup.py # Assembles Crew with all agents & tasks
├── logging/
│ └── logger.py # Handles file-based logging
├── logs/
│ └── TechPod.log # Log file for TechPod Research Agent
├── main.py # Entry point to kickoff MVP crew
└── environment.yml # Conda environment file