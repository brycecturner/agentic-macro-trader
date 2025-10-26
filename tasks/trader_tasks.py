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
            "Using the following summarized macro research, generate one possible "
            "trading hypothesis and portfolio strategy:"
            f"{research_summary_json}"
            "Your output should:"
            "- Propose one distinct macro hypotheses"
            "- Suggest corresponding trade expressions (e.g., equities, rates, spreads, FX, commodities)"
            "- Include reasoning (macro drivers, risks, catalysts)"
            "- Identify key risk factors and alternative scenarios"
            "- Provide a clear investment thesis"
            "- Give time horizon for the trade"
            "- The hypothiesis should be actionable, specific, and creative."
            "- It must be suitable for implementation by a portfolio construction agent."
            f"{get_current_date_for_prompting()}"
        ),
        expected_output=(
            "The output must strictly follow this JSON schema:"
            f"{schema}"
        ),
        verbose=True,
        async_execution=True,
    )

    logger.info("Trader task created successfully.")
    return task
