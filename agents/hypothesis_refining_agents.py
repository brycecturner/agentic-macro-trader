from crewai import Agent
from tools.research_tools import research_tools, serper_logic_for_query
from utils.utils import load_schema, get_current_date_for_prompting
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
            f"{get_current_date_for_prompting()}"
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
            f"{get_current_date_for_prompting()}"

        ),
        allow_delegation=False,
        tools=research_tools(),
        verbose=True
    )

def create_falsification_agent():
    """
    Agent that determines falsification conditions for a refined hypothesis.
    """
    logger.info("Creating Falsification Agent")

    return Agent(
        role="Portfolio Falsification Analyst",
        goal="Define conditions that would falsify a refined trade hypothesis.",
        backstory=(
            "You are a risk-focused macro strategist. Your role is to identify the conditions "
            "under which a refined trade thesis should be considered invalid. This includes "
            "index thresholds, bundles of indices, macroeconomic data surprises, news/policy headlines, "
            "or unexpected exogenous shocks. Your output should be structured and testable."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True
    )
