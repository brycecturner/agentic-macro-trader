import logging
from crewai import Crew
from tasks.research_tasks import create_research_task
from tasks.trader_tasks import create_trader_task

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('logs/crew.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(handler)

def create_crew() -> Crew:
    logger.info("Starting crew creation process...")

    # Step 1: Create the research task
    research_task = create_research_task()
    logger.info("Research task created.")

    # Step 2: Use research task as context for trader task
    trader_task = create_trader_task()
    logger.info("Trader task created with research task as context.")

    # Step 3: Assemble the crew
    crew = Crew(
        agents=[research_task.agent, trader_task.agent],
        tasks=[research_task, trader_task],
        verbose=True
    )
    logger.info("Crew assembled with 2 agents and 2 tasks.")

    return crew
