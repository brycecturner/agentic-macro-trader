import json

def join_outputs_as_json(results: list[tuple[str, str, str]]) -> str:
    data = [
        {"task": task_desc, "agent": agent_role, "output": output.raw}
        for task_desc, agent_role, output in results
    ]
    return json.dumps(data, indent=2)
