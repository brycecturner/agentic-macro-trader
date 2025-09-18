import logging
from crewai import Task
from utils.utils import load_schema
from agents.implementation_agents import create_portfolio_agent

logger = logging.getLogger(__name__)

def create_portfolio_task():
    """
    Task for constructing a portfolio from refined trade hypotheses.
    """

    logger.info("Creating Portfolio Construction Task")
    
    schema = load_schema("schemas/portfolio.json")

    return Task(
        description=(
            dklasdfkl;jasdfjsadf # This needs to be fixed
            "Input: a JSON array of refined trade hypotheses produced by the previous agent. "
            "Each hypothesis includes a unique `name`, `thesis`, `confidence` (0-1), and any supporting data.\n\n"
            "Goal: construct a single portfolio object that strictly conforms to the provided portfolio JSON schema. "
            "Produce machine-parseable JSON only — do not include explanatory text outside the JSON.\n\n"
            "Requirements:\n"
            "- For each hypothesis that should be represented in the portfolio, include an entry under `positions` with: `ticker` (string), `weight` (number, sum of weights == 1.0), and `rationale` (string) that explicitly references the hypothesis `name`.\n"
            "- Provide a top-level `objective` field describing the portfolio's investment objective (max return, risk parity, income, etc.).\n"
            "- Include portfolio-level risk metrics in a `risk` object with at least: `expected_return` (annualized %), `volatility` (annualized %), and `max_drawdown` (%).\n"
            "- Add a `constraints` array listing any constraints applied (e.g., sector limits, max position size).\n"
            "- The `name` property of the portfolio must match the hypothesis `name` exactly when the portfolio is derived from a single hypothesis; if multiple hypotheses are combined, use a descriptive compound name and list source hypothesis names in `sources`.\n\n"
            "Validation rules and style constraints:\n"
            "- Output must be valid JSON and must validate against the `portfolio.json` schema loaded by the task.\n"
            "- Numeric fields must use numbers (not strings). Percentages should be expressed as decimals (e.g., 0.12 for 12%).\n"
            "- Weights must be normalized to sum to 1.0 (allow a tolerance of ±0.001).\n"
            "- Keep `rationale` entries concise (1-3 sentences) and tie them directly to hypothesis evidence and confidence scores.\n\n"
            "Failure modes:\n"
            "- If a hypothesis lacks a clear tradeable ticker, either map it to a proxy ETF or omit it and note the omission in the `notes` field inside the JSON.\n"
            "- If confidence scores are low (<0.4), reflect this in lower weights or exclude the hypothesis; explain choices in `rationale`.\n\n"
            "Return: a single JSON object that matches the task's `expected_output` schema exactly (no extra top-level fields)."
        ),
        agent=create_portfolio_agent(),
        expected_output=(
            "The output must strictly follow this JSON schema:\n"
            f"{schema}"
            "where the name property matches the hypothesis name exactly."
        ),
    )
