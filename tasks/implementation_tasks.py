import logging
from crewai import Task
from utils.utils import load_schema
from agents.implementation_agents import create_portfolio_agent

logger = logging.getLogger(__name__)

def create_portfolio_task():
    """
    Task for constructing a portfolio from refined trade hypotheses.
    """

    logger.info("Creating Portfolio Construction Task")
    
    schema = load_schema("schemas/portfolio.json")

    return Task(
        description=(
            "You are given a set of refined trade hypotheses. "
            "Your job is to translate them into a structured portfolio, "
            "including asset tickers, weights, and rationale. "
            "You should also provide portfolio-level risk metrics and "
            "a clear portfolio objective.\n\n"
            f"Refined Hypotheses comes from the previous agent.\n"
            "Return output strictly matching the portfolio_schema."
        ),
        agent=create_portfolio_agent(),
        expected_output=(
            "The output must strictly follow this JSON schema:\n"
            f"{schema}"
            "where the name property matches the hypothesis name exactly."
        ),
    )
