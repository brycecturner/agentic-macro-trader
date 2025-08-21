from crewai import Agent
from tools.research_tools import research_tools
import logging

logger = logging.getLogger(__name__)

def create_critic_agent():
    logger.info("Creating Critic Agent")
    return Agent(
        role="Hypothesis Critic",
        goal="Critically evaluate one trading hypothesis for weaknesses and risks.",
        backstory=(
            "You are a skeptical and detail-oriented risk manager at a hedge fund. "
            "You identify flaws, hidden assumptions, and risks in hypotheses "
            "before any capital is allocated."
        ),
        allow_delegation=False,
        tools=research_tools(),
        verbose=True
    )


def create_refiner_agent():
    logger.info("Creating Refiner Agent")
    return Agent(
        role="Hypothesis Refiner",
        goal="Refine a single trading hypothesis into a more robust and testable trade thesis.",
        backstory=(
            "You are a senior strategist who improves ideas by addressing critiques. "
            "You make hypotheses more resilient and ensure they conform to the trade_thesis schema."
        ),
        allow_delegation=False,
        tools=research_tools(),
        verbose=True
    )
