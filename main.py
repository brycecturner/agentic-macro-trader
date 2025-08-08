import os
from dotenv import load_dotenv #type:ignore
import asyncio
from crew.run_parallel_crews import run_parallel_crews
from utils.utils import join_outputs_as_json

# from crewai_tools import SerperDevTool


from tasks.research_tasks import (
    create_research_fed_policy_task,
    create_research_banking_risk_task,
    create_research_global_capital_flows_task,
    create_research_fiscal_policy_task,
    create_research_macro_growth_task,
    create_research_macro_inflation_task,
)
from agents.research_agents import (
    create_fed_policy_research_agent,
    create_banking_risk_research_agent,
    create_global_capital_flows_research_agent,
    create_fiscal_policy_research_agent,
    create_macro_growth_research_agent,
    create_macro_inflation_research_agent,
)

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Entry point
if __name__ == "__main__":
    #nest_asyncio.apply()  # Useful for notebooks or environments that complain about running loops



    # tool = SerperDevTool()
    # result = tool.run("Latest Fed monetary policy statements and analysis")
    # print(result)

    results = asyncio.run(run_parallel_crews([
        (create_research_fed_policy_task(), create_fed_policy_research_agent()),
        (create_research_banking_risk_task(), create_banking_risk_research_agent()),
        (create_research_global_capital_flows_task(), create_global_capital_flows_research_agent()),
        (create_research_fiscal_policy_task(), create_fiscal_policy_research_agent()),
        (create_research_macro_growth_task(), create_macro_growth_research_agent()),
        (create_research_macro_inflation_task(), create_macro_inflation_research_agent()),
    ]))

    for (task, agent, output) in results:
        print("")
        print("-----")
        print(f"{agent}")
        print(output)

    result_json = join_outputs_as_json(results)
    with open("research_summary.json", "w") as f:
        f.write(result_json)
