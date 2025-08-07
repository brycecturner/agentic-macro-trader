

import logging
from crewai import Agent

# Set up logging
logger = logging.getLogger("ManagerAgentLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/manager_agent.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def create_manager_agent():
    logger.info("Initializing manager research agent.")

    manager = Agent(
        role="Project Manager",
        goal=(
            "Efficiently manage the crew and ensure high-quality task completion"
        ),
        backstory=(
            "You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success."
            "Your role is to coordinate the efforts of the crew members." 
            "You ensure that each task is completed to the highest standard."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[],  # Add scraping or summarization tools if desired
    )

    logger.info("manager research agent created.")
    return manager

