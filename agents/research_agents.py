import logging
from crewai import Agent

# Set up logging
logger = logging.getLogger("TechPodLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/research_agent.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def create_research_agent():
    logger.info("Initializing TechPod research agent.")

    tech_pod = Agent(
        role="TechPod Research Analyst",
        goal=(
            "Identify and summarize key developments, earnings reports, and macroeconomic news."
        ),
        backstory=(
            "You are a specialized research analyst working in the Macro-Research division of an AI-powered hedge fund. "
            "Your job is to scan, distill, and contextualize recent events."
            "Your output will guide downstream trading decisions."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[],  # Add scraping or summarization tools if desired
    )

    logger.info("Research agent created.")
    return tech_pod

# agents/banking_risk_research_agent.py


def create_banking_risk_research_agent() -> Agent:
    logger.info("Creating banking system fragility research agent...")

    agent = Agent(
        role="Banking System Risk Analyst",
        goal=(
            "Monitor and evaluate the stability of the banking sector by identifying early warning signs "
            "of systemic risk such as declining bank reserves, rising loan defaults, interbank stress, "
            "or liquidity shortages."
        ),
        backstory=(
            "You are a macroeconomic researcher at a hedge fund tasked with identifying risks in the banking sector. "
            "You specialize in analyzing regulatory filings, central bank reports, and market data to anticipate "
            "systemic financial stress. Your insights feed directly into portfolio risk controls and hedging strategies."
        ),
        allow_delegation=False,
        verbose=True,
        tools=[],  # Optional, add more if needed
    )

    logger.info("Banking system risk research agent created successfully.")
    return agent


def create_fed_policy_research_agent() -> Agent:
    logger.info("Creating Federal Reserve monetary policy research agent...")

    agent = Agent(
        role="Federal Reserve Policy Analyst",
        goal=(
            "Track, interpret, and forecast the Federal Reserve’s monetary policy decisions, including interest rate changes, "
            "quantitative tightening or easing, balance sheet positioning, and public communications from FOMC members."
        ),
        backstory=(
            "You are a macroeconomic researcher at a hedge fund focused exclusively on central bank policy. "
            "You analyze FOMC statements, meeting minutes, press conferences, and speeches from Fed officials. "
            "You combine this with market-based indicators such as the Fed Funds futures curve, inflation breakevens, "
            "and Treasury yields to forecast likely policy shifts. Your insights help inform positioning across rates, FX, and equities."
        ),
        allow_delegation=False,
        verbose=True,
        tools=[],  # Extend with other document or data tools if needed
    )

    logger.info("Federal Reserve policy research agent created successfully.")
    return agent
