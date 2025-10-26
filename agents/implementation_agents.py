from crewai import Agent
from tools.research_tools import research_tools, serper_logic_for_query
from utils.utils import load_schema, get_current_date_for_prompting
import logging


logger = logging.getLogger(__name__)


def create_portfolio_agent():
    """
    Agent that takes refined trade hypotheses and constructs a portfolio.
    """
    logger.info("Creating Portfolio Construction Agent")

    return Agent(
        role="Portfolio Construction Strategist",
        goal="Translate refined trade hypotheses into an actionable portfolio with weights and risk controls.",
        backstory=(
            "You are an experienced portfolio manager who specializes in multi-asset allocation. "
            "Given a single refined trade hypotheses, you build a coherent portfolio "
            "that balances conviction with diversification and risk management. "
            "You provide clear justifications for each position and its weight in the portfolio."
        ),
        allow_delegation=False,
        verbose=True,
    )