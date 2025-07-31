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
            "Identify and summarize key developments, earnings reports, and macroeconomic "
            "news affecting top technology companies."
        ),
        backstory=(
            "You are a specialized research analyst working in the TechPod division of an AI-powered hedge fund. "
            "Your job is to scan, distill, and contextualize recent events in the technology sector. "
            "Your output will guide downstream trading decisions."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[],  # Add scraping or summarization tools if desired
    )

    logger.info("TechPod research agent created.")
    return tech_pod
