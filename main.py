import os
import asyncio
from dotenv import load_dotenv  # type: ignore

from crew.run_parallel_crews import run_parallel_crews
from utils.utils import join_outputs_as_json

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

# NEW trader imports
from tasks.trader_tasks import create_trader_task
from agents.trader_agent import create_trader_agent


# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


async def main():
    # 1. Run research agents in parallel
    results = await run_parallel_crews([
        (create_research_fed_policy_task(), create_fed_policy_research_agent()),
        # (create_research_banking_risk_task(), create_banking_risk_research_agent()),
        # (create_research_global_capital_flows_task(), create_global_capital_flows_research_agent()),
        # (create_research_fiscal_policy_task(), create_fiscal_policy_research_agent()),
        # (create_research_macro_growth_task(), create_macro_growth_research_agent()),
        # (create_research_macro_inflation_task(), create_macro_inflation_research_agent()),
    ])

    # # 2. Print outputs for visibility
    # for (task, agent, output) in results:
    #     print("\n-----")
    #     print(f"{agent}")
    #     print(output)

    # 3. Save research results JSON
    result_json = join_outputs_as_json(results)
    with open("results/research_summary.json", "w") as f:
        f.write(result_json)

    # 4. Run trader agent on the research results
    # trader_task = create_trader_task(result_json)
    # trader_agent = create_trader_agent()
    trader_output = await run_parallel_crews([
        (create_trader_task(result_json), create_trader_agent()),
    ])

    # 5. Save trader hypotheses
    with open("results/trader_hypotheses.json", "w") as f:
        f.write(join_outputs_as_json(trader_output))

    print("\n===== Trader Hypotheses =====")
    print(trader_output)


if __name__ == "__main__":
    asyncio.run(main())
