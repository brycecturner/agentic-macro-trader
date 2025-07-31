import logging
from crewai import Agent
from tools.get_current_stock_price import getTickerPrice

# Set up logging
logger = logging.getLogger("TraderAgentLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/trader_agent.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def create_trader_agent():
    logger.info("Initializing Trader Agent.")

    trader_agent = Agent(
        role="Trader",
        goal=(
            "Evaluate research summaries to decide whether to enter or exit stock positions "
            "for the current trading day. Follow basic trading logic for an MVP."
        ),
        backstory=(
            "You are a systematic trader operating within an AI-driven hedge fund. You receive input from the Research Agent."
            "For each of the stocks sent to you from the research agent, query the most recent stock price use getTickerPrice tool."
            "You make trade decisions accordingly using price data and research input."
            "For this MVP, you log trade decisions instead of executing them."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[getTickerPrice],  # Add broker API tools in future iterations
    )

    logger.info("Trader Agent created.")
    return trader_agent
