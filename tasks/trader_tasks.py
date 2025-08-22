import json
import logging
from crewai import Task
from agents.trader_agent import create_trader_agent
from utils.utils import get_current_date_for_prompting, load_schema


logger = logging.getLogger(__name__)

def create_trader_task(research_summary_json: dict) -> Task:
    logger.info("Creating trader task...")

    schema = load_schema("schemas/raw_trade_thesis.json")

    task = Task(
        agent = create_trader_agent(),
        description=(
            "Using the following summarized macro research, generate possible "
            "trading hypotheses and portfolio strategies:\n"
            f"{research_summary_json}\n\n"
            "Your output should:\n"
            "- Propose 2–3 distinct macro hypotheses\n"
            "- Suggest corresponding trade expressions (e.g., equities, rates, FX, commodities)\n"
            "- Include reasoning (macro drivers, risks, catalysts)\n"
            "- Identify key risk factors and alternative scenarios\n"
            f"{get_current_date_for_prompting()}"
        ),
        expected_output=(
            "The output must strictly follow this JSON schema:\n"
            f"{schema}"
        ),
        verbose=True,
        async_execution=True,
    )

    logger.info("Trader task created successfully.")
    return task
