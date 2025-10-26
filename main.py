import os
import asyncio
from dotenv import load_dotenv  # type: ignore
import json
import logging

from crew.run_parallel_crews import run_parallel_crews
from utils.utils import join_outputs_as_json,normalize_trader_hypotheses

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

# implementation imports
from tasks.implementation_tasks import create_portfolio_task
from agents.implementation_agents import create_portfolio_agent

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MainLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/main.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

async def refine_hypothesis(hypotheses: list[dict]) -> list[tuple[str, str, str]]:
    """Run critic + refiner agents on each hypothesis in parallel."""
    crews = []
    
    # for hyp in hypotheses:
    logger.info(f"Refining hypothesis: {hypotheses}")
    hyp_json = json.dumps(hypotheses)

    crews.append((create_critic_task(hyp_json), create_critic_agent()))
    crews.append((create_refiner_task(hyp_json), create_refiner_agent()))
    crews.append((create_portfolio_task(), create_portfolio_agent()))
    
        #TODO - Implement falsification agent/task
        #crews.append(create_falsification_task(), create_falsification_agent())

        #TODO 
        #crews.append(create_portfolio_task(hyp_json), create_portfolio_agent()))
        #crews.append(create_risk_management_task(hyp_json), create_risk_management_agent()))
        #crews.append(create_implementation_task(hyp_json), create_implementation_agent()))
        
    results = await run_parallel_crews(crews)
    return results

async def main():
    # 1. Run research agents in parallel
    research_results = await run_parallel_crews([
        (create_research_fed_policy_task(), create_fed_policy_research_agent()),
        (create_research_banking_risk_task(), create_banking_risk_research_agent()),
        (create_research_global_capital_flows_task(), create_global_capital_flows_research_agent()),
        (create_research_fiscal_policy_task(), create_fiscal_policy_research_agent()),
        (create_research_macro_growth_task(), create_macro_growth_research_agent()),
        (create_research_macro_inflation_task(), create_macro_inflation_research_agent()),
    ])

    # 2. Save research results JSON
    research_result_json = join_outputs_as_json(research_results)
    with open("results/research_summary.json", "w") as f:
        f.write(research_result_json)
    logger.info("Saved research summary to results/research_summary.json")

    # 3. Run trader agent on the research results
    trader_results = await run_parallel_crews([
        (create_trader_task(research_result_json), create_trader_agent()),
    ])

    logger.info(f"Trader output: {trader_results[0]}")

    _, _, trader_hypothesis = trader_results[0]
    trader_hypothesis = trader_hypothesis.raw

    with open("results/initial_hypothesis.json", "w") as f:
        f.write(trader_hypothesis)
    logger.info("Saved intitial trader hypothesis to results/initial_hypothesis.json")

    logger.info("Normalized trader hypotheses.")
    logger.info(f"Trader hypotheses type: {type(trader_hypothesis)}")
    logger.info(f"Trader hypotheses: {trader_hypothesis}")

    # 5. Run critic + refiner agents for each hypothesis
    if trader_hypothesis:
        logger.info(f"Refining trader hypothesis...")
    
        refined_hypothesis = await refine_hypothesis(trader_hypothesis)

        for (_, agent, crew_out) in refined_hypothesis:
            if "Refiner" in str(agent):  # Save refiner results
                try:
                    refined_output = json.loads(crew_out.raw)
                except Exception:
                    refined_output = {"raw": crew_out.raw}

            elif "Critic" in str(agent):  # Save critic results separately
                try:
                    critic_output = json.loads(crew_out.raw)
                except Exception:
                    critic_output = {"raw": crew_out.raw}
        
            elif "Portfolio Construction" in str(agent):
                try:
                    portfolio_output = json.loads(crew_out.raw)
                except Exception:
                    portfolio_output = {"raw": crew_out.raw}

        logger.info(f"Refined Hypotheses: {refined_output}")
        
        # Save refined trade theses
        with open("results/refined_hypothesis.json", "w") as f:
            json.dump(refined_output, f, indent=2)

        # Optional: save critics for debugging
        with open("results/critic_feedback.json", "w") as f:
            json.dump(critic_output, f, indent=2)
        
        # Save portfolio output
        with open("results/portfolio.json", "w") as f:
            json.dump(portfolio_output, f, indent=2)

        logger.info("Saved refined hypotheses and critic feedback")
        
    
if __name__ == "__main__":
    asyncio.run(main())
