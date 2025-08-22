# tasks/refine_hypothesis_tasks.py

from crewai import Task
import logging
from tools.research_tools import research_tools, serper_logic_for_query
from utils.utils import get_current_date_for_prompting, load_schema
from agents.hypothesis_refining_agents import create_critic_agent, create_refiner_agent

logger = logging.getLogger(__name__)



def create_critic_task(hypothesis_json: str):
    logger.info("Creating Critic Task for one hypothesis")
    return Task(
        agent=create_critic_agent(),
        description=(
            f"You are given ONE trading hypothesis in JSON format: {hypothesis_json}. "
            "Critique this hypothesis by identifying weaknesses, risks not accounted for, "
            "and assumptions that may fail."
            f"{serper_logic_for_query()}"
        ),
        expected_output="A summary of critiques.",
        verbose = True,
        async_execution = True,
        tools = research_tools()
    )


def create_refiner_task(hypothesis_json: str):
    logger.info("Creating Refiner Task for one hypothesis")

    schema = load_schema("schemas/final_trade_thesis.json")

    return Task(
        agent = create_refiner_agent(),
        description=(
            f"You are given ONE trading hypothesis: {hypothesis_json}, and ONE critique from the previous agent."
            f"Refine the hypothesis into a more robust trade thesis by addressing the critiques."
            "Your output should:"
            "- Propose one refined, distinct macro hypotheses"
            "- Describe the macro drivers and risks"
            "- Suggest corresponding trade expressions (e.g., equities, rates, FX, commodities)"
            "- Include reasoning (macro drivers, risks, catalysts)"
            "- Identify key risk factors and alternative scenarios"
            "- Provide a clear investment thesis"
            # f"{serper_logic_for_query()}"
            f"{get_current_date_for_prompting()}"
        ),
        expected_output=(
            "The output must strictly follow this JSON schema:\n"
            f"{schema}"
            "where the name property matches the hypothesis name exactly."
        ),
        verbose = True,
        async_execution = True,
        # tools = research_tools()
    )
