import logging
from crewai import Crew
import asyncio


logger = logging.getLogger(__name__)

async def run_parallel_crews(task_agent_pairs: list[tuple]) -> list[str]:
    """
    Runs multiple (agent, task) pairs in parallel and returns their outputs.

    Args:
        task_agent_pairs (list of tuples): Each tuple should contain a Task and its corresponding Agent.

    Returns:
        List of task outputs (strings).
    """
    logger.info("Starting parallel execution of research crews...")

    async def run_single_crew(task, agent):
        logger.info(f"Launching crew for agent: {agent.role}")

        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True
        )
        output = crew.kickoff()
        logger.info(f"Completed crew for agent: {agent.role}")
        return (task.description, agent.role, output)

    # Create coroutine tasks
    coroutines = [run_single_crew(task, agent) for task, agent in task_agent_pairs]

    # Gather all results
    results = await asyncio.gather(*coroutines)

    logger.info("All research crews completed.")
    return results