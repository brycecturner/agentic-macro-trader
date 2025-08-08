import json
from datetime import datetime


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
