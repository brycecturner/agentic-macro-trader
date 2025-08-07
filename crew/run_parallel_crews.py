import logging
from crewai import Crew
import asyncio

from tasks.research_tasks import (
    create_research_fed_policy_task,
    create_research_banking_risk_task
)
from agents.research_agents import (
    create_fed_policy_research_agent,
    create_banking_risk_research_agent
)

logger = logging.getLogger(__name__)

def create_parallel_crews():
    logger.info("Initializing creation of parallel research crews...")

    # Create tasks
    logger.info("Creating Fed policy research task and agent.")
    fed_task = create_research_banking_risk_task()

    logger.info("Creating banking system risk research task and agent.")
    bank_task = create_research_banking_risk_task()

    # Assemble crews
    fed_crew = Crew(
        agents=[fed_task.agent],
        tasks=[fed_task],
        verbose=True
    )
    logger.info("Fed policy research crew assembled.")

    bank_crew = Crew(
        agents=[bank_task.agent],
        tasks=[bank_task],
        verbose=True
    )
    logger.info("Banking risk research crew assembled.")

    logger.info("Both research crews created successfully.")
    return fed_crew, bank_crew


async def run_parallel_crews():
    fed_crew, bank_crew = create_parallel_crews()

    # Run both crews concurrently
    results = await asyncio.gather(
        asyncio.to_thread(fed_crew.kickoff),
        asyncio.to_thread(bank_crew.kickoff)
    )

    fed_output, bank_output = results
    return fed_output, bank_output