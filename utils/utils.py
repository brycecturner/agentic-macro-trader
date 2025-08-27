import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def join_outputs_as_json(results: list[tuple[str, str, str]]) -> str:
    data = [
        {"task": task_desc, "agent": agent_role, "output": output.raw}
        for task_desc, agent_role, output in results
    ]
    return json.dumps(data, indent=2)


def get_current_date_for_prompting() -> str:
    """
    Returns a string with the current date in YYYY-MM-DD format
    to be injected into agent or task prompts.
    """
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    return f"Today's date is {today_str}. Please use this as the current date for all time-sensitive reasoning."

def load_schema(path: str) -> dict:
    """Generic schema loader for tasks/agents."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load schema from {path}: {e}")
        raise


def normalize_trader_hypotheses(raw):
    """
    Normalize the trader agent output to always return a list of hypotheses.
    Handles cases where output is a list, a dict with a list, or a JSON string.
    """
    # If it's a string, try to parse as JSON
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except Exception:
            return []

    # If it's a dict with a list under a key (e.g., 'items' or 'hypotheses')
    if isinstance(raw, dict):
        for key in ['items', 'hypotheses', 'data']:
            if key in raw and isinstance(raw[key], list):
                return raw[key]
        # If dict itself is a single hypothesis, wrap in list
        return [raw]

    # If it's already a list
    if isinstance(raw, list):
        return raw

    # Fallback: wrap anything else in a list
    return [raw]