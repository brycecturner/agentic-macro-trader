import logging
from crewai import Task
from agents.research_agent import create_research_agent

# Set up logging
logger = logging.getLogger("TechPodTaskLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/research_task.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def create_research_task() -> Task:
    logger.info("Creating research task for TechPod agent.")

    tech_pod_agent = create_research_agent()

    task = Task(
        agent=tech_pod_agent,
        description=(
            "Research the top 5 technology companies by market cap (e.g., AAPL, MSFT, NVDA, GOOGL, AMZN). "
            "Summarize the most recent news, earnings reports, or macroeconomic developments affecting these firms. "
            "Your analysis should include both qualitative and quantitative insights when available."
        ),
        expected_output=(
            "A concise summary (3–5 bullet points per company) outlining key events, their market impact, and any "
            "potential signals for future price movement or volatility."
        ),
        verbose=True,
    )

    logger.info("Research task created successfully.")
    return task
