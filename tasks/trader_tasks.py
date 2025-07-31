import logging
from crewai import Task
from agents.trader_agent import create_trader_agent

# Set up logging
logger = logging.getLogger("TraderTaskLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/trader_task.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def create_trader_task() -> Task:
    logger.info("Creating trader task based on research output.")

    trader_agent = create_trader_agent()

    task = Task(
        agent=trader_agent,
        description=(
            "Using the provided research summary and recent stock price, analyze the key signals and determine simple trading actions "
            "for each of the top 5 tech stocks (buy, hold, or sell). Consider macroeconomic factors, earnings reports, "
            "and recent market trends highlighted in the research."
        ),
        expected_output=(
            "A trading decision, formatted as ticker - recommendation - current price - 2 sentence justification per pick."
        ),
        
        verbose=True,
    )

    logger.info("Trader task created successfully.")
    return task
