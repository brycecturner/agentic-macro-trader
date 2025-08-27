import os
import asyncio
from dotenv import load_dotenv  # type: ignore
import json
import logging

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

# rader imports
from tasks.trader_tasks import create_trader_task
from agents.trader_agent import create_trader_agent

# refining imports
from agents.hypothesis_refining_agents import (
    create_critic_agent, 
    create_refiner_agent,
    create_falsification_agent
)
from tasks.refine_hypothesis_tasks import (
    create_critic_task, 
    create_refiner_task,
    create_falsification_task
)

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def refine_hypotheses(hypotheses: list[dict]) -> list[tuple[str, str, str]]:
    """Run critic + refiner agents on each hypothesis in parallel."""
    crews = []
    for hyp in hypotheses:
        hyp_json = json.dumps(hyp)

        crews.append((create_critic_task(hyp_json), create_critic_agent()))
        crews.append((create_refiner_task(hyp_json), create_refiner_agent()))
        
        #TODO - Implement falsification agent/task
        #crews.append(create_falsification_task, create_falsification_agent())

        #TODO 
        #crews.append(create_portfolio_task(hyp_json), create_portfolio_agent()))
        #crews.append(create_risk_management_task(hyp_json), create_risk_management_agent()))
        #crews.append(create_implementation_task(hyp_json), create_implementation_agent()))
        
    results = await run_parallel_crews(crews)
    return results


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

    # 2. Save research results JSON
    result_json = join_outputs_as_json(results)
    with open("results/research_summary.json", "w") as f:
        f.write(result_json)
    logger.info("Saved research summary to results/research_summary.json")

    # 3. Run trader agent on the research results
    trader_output = await run_parallel_crews([
        (create_trader_task(result_json), create_trader_agent()),
    ])
    _, _, crew_out = trader_output[0]

    # 4. Save trader hypotheses
    trader_hypotheses = None
    with open("results/trader_hypotheses.json", "w") as f:
        if isinstance(crew_out.raw, str):
            try:
                trader_hypotheses = json.loads(crew_out.raw)
                json.dump(trader_hypotheses, f, indent=2)
            except Exception:
                f.write(crew_out.raw)
        else:
            trader_hypotheses = crew_out.raw
            json.dump(trader_hypotheses, f, indent=2)

    logger.info("Saved trader hypotheses to results/trader_hypotheses.json")

    # 5. Run critic + refiner agents for each hypothesis
    if trader_hypotheses:
        logger.info(f"Refining {len(trader_hypotheses['items'])} trader hypotheses...")
    
        refined_hypotheses = await refine_hypotheses(trader_hypotheses['items'])

        refined_outputs = []
        critic_outputs = []

        for (_, agent, crew_out) in refined_hypotheses:
            if "Refiner" in str(agent):  # Save refiner results
                try:
                    refined_outputs.append(json.loads(crew_out.raw))
                except Exception:
                    refined_outputs.append({"raw": crew_out.raw})

            elif "Critic" in str(agent):  # Save critic results separately
                try:
                    critic_outputs.append(json.loads(crew_out.raw))
                except Exception:
                    critic_outputs.append({"raw": crew_out.raw})

        # Save only refined trade theses
        with open("results/refined_hypotheses.json", "w") as f:
            json.dump(refined_outputs, f, indent=2)

        # Optional: save critics for debugging
        with open("results/critic_feedback.json", "w") as f:
            json.dump(critic_outputs, f, indent=2)

        logger.info("Saved refined hypotheses and critic feedback")
        
    


if __name__ == "__main__":
    asyncio.run(main())
