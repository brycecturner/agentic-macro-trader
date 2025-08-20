import logging
from crewai import Agent
from utils.utils import get_current_date_for_prompting
from tools.research_tools import research_tools

logger = logging.getLogger(__name__)

def create_trader_agent() -> Agent:
    logger.info("Creating trader / hypothesis generator agent...")

    agent = Agent(
        role="Multi-Strategy Portfolio Hypothesis Generator",
        goal=(
            "Integrate macroeconomic research into actionable investment hypotheses and portfolio strategies. "
            "Generate coherent trade ideas that reflect potential risks, opportunities, and regime shifts."
        ),
        backstory=(
            "You are a hedge fund strategist who specializes in turning complex macro research into investable "
            "trade hypotheses. You analyze signals from global capital flows, central bank policies, fiscal dynamics, "
            "and systemic risks to propose coherent portfolio strategies."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),  # optional, e.g., if you want it to validate with Serper
    )

    logger.info("Trader / hypothesis generator agent created successfully.")
    return agent
