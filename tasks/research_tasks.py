import logging
from crewai import Task
# from agents.research_agents import create_fed_policy_research_agent, create_banking_risk_research_agent

from agents.research_agents import (
    create_fed_policy_research_agent,
    create_banking_risk_research_agent,
    create_global_capital_flows_research_agent,
    create_fiscal_policy_research_agent,
    create_macro_growth_research_agent,
    create_macro_inflation_research_agent,
)

# Set up logging
logger = logging.getLogger("TechPodTaskLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/research_task.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def create_research_fed_policy_task() -> Task:
    logger.info("Creating research task on fed policy.")    

    task = Task(
        agent=create_fed_policy_research_agent(),
        description=(
            "Conduct comprehensive research to assess the likely path of Federal Reserve monetary policy, "
            "including interest rate decisions, balance sheet adjustments, and forward guidance. "
            "Scrape the web and analyze relevant documents such as FOMC meeting minutes, speeches by Fed officials, "
            "economic data releases (e.g., CPI, PCE, unemployment), and credible media coverage. "
            "Identify consensus expectations, recent Fed signaling, and any shifts in tone or language. "
            "Highlight the most probable policy moves over the next 1–3 FOMC meetings, and outline key risks or uncertainties "
            "that could influence the trajectory."
        ),
        expected_output=(
            "A structured summary including:"
            "- Key fragility indicators and which institutions or regions are most exposed"
            "- 2–3 specific examples of concerning trends"
            "- Citations of relevant data or sources"
            "- A brief commentary on potential contagion channels or systemic implications"
        ),
        verbose=True,
        async_execution = True,
        
    )

    logger.info("Fed Policy Research task created successfully.")
    return task

def create_research_banking_risk_task() -> Task:   
    logger.info("Creating research task on banking fragility.") 
    
    task  = Task(
    agent=create_banking_risk_research_agent(),  
    description=(
        "Research signs of fragility within the U.S. banking system, focusing on small and mid-sized banks. "
        "Identify early warning indicators such as elevated unrealized losses, deposit flight risk, commercial real estate exposure, "
        "or tightening liquidity conditions. Use credible sources like FDIC, Federal Reserve, and major financial media (WSJ, Bloomberg)."
    ),
    expected_output=(
        "A structured summary including:"
        "- Key fragility indicators and which institutions or regions are most exposed"
        "- 2–3 specific examples of concerning trends"
        "- Citations of relevant data or sources"
        "- A brief commentary on potential contagion channels or systemic implications"
    ),
    tools=[],  
    verbose=True,
    async_execution = True
    )

    logger.info("Banking Fragility Research task created successfully.")

    return task

def create_research_global_capital_flows_task() -> Task:
    logger.info("Creating research task on global capital flows.")    

    task = Task(
        agent=create_global_capital_flows_research_agent(),
        description=(
            "Investigate recent trends in global capital flows, focusing on cross-border investment patterns, "
            "emerging market inflows/outflows, and sovereign wealth fund activity. Scrape financial news, "
            "international reports (e.g., IMF, BIS), and analyze recent data from capital markets. Identify which regions or asset classes "
            "are attracting or losing capital, and the macroeconomic drivers behind these shifts."
        ),
        expected_output=(
            "A structured summary including:\n"
            "- Key capital flow trends and their regional or asset-specific concentration\n"
            "- 2–3 illustrative examples with data-driven support\n"
            "- Relevant institutional commentary or policy responses\n"
            "- Potential implications for exchange rates, bond markets, or systemic liquidity"
        ),
        verbose=True,
        async_execution=True,
    )
    logger.info("Global Capital Flows task created successfully.")
    return task

def create_research_fiscal_policy_task() -> Task:
    logger.info("Creating research task on fiscal policy and sovereign balance sheets.")    

    task = Task(
        agent=create_fiscal_policy_research_agent(),
        description=(
            "Analyze fiscal policy developments and sovereign balance sheet health across major economies. "
            "Focus on debt issuance, interest expense trends, budget deficits, and government responses to economic slowdowns. "
            "Scrape relevant government reports, IMF data, and market commentary. Highlight countries with rising fiscal risks, "
            "and explore the impact of those risks on bond markets and policy flexibility."
        ),
        expected_output=(
            "A structured summary including:\n"
            "- Overview of fiscal risk indicators in key economies\n"
            "- 2–3 examples of countries with deteriorating or improving fiscal trends\n"
            "- Commentary on potential rating actions, crowding out effects, or inflationary pressures\n"
            "- Citations of official data or credible reports"
        ),
        verbose=True,
        async_execution=True,
    )
    logger.info("Fiscal Policy task created successfully.")
    return task

def create_research_macro_growth_task() -> Task:
    logger.info("Creating macro indicator task 1.")    

    task = Task(
        agent=create_macro_growth_research_agent(),
        description=(
            "Monitor and analyze leading macroeconomic indicators, such as PMI data, industrial production, durable goods orders, "
            "and business sentiment indexes. Identify early signals of economic turning points or regional divergence. "
            "Scrape economic dashboards, institutional reports, and financial commentary."
        ),
        expected_output=(
            "A structured summary including:\n"
            "- Key changes in macro indicators across major regions\n"
            "- Notable surprises (positive or negative) in recent releases\n"
            "- Implications for growth forecasts or risk sentiment\n"
            "- Sourced commentary from institutions or analysts"
        ),
        verbose=True,
        async_execution=True,
    )
    logger.info("Macro Indicators Task 1 created successfully.")
    return task

def create_research_macro_inflation_task() -> Task:
    logger.info("Creating macro indicator task 2.")    

    task = Task(
        agent=create_macro_inflation_research_agent(),
        description=(
            "Track labor market and inflation-related macro data, including CPI, PPI, wage growth, labor force participation, "
            "and job openings. Assess the balance between inflation pressure and employment strength. "
            "Pull from government releases, economic research, and media summaries."
        ),
        expected_output=(
            "A structured summary including:\n"
            "- Trends in inflation vs. labor market strength\n"
            "- Any signs of wage-price spirals or disinflation\n"
            "- Market or policy expectations based on recent prints\n"
            "- Cited data sources (e.g., BLS, media, analyst reports)"
        ),
        verbose=True,
        async_execution=True,
    )
    logger.info("Macro Indicators Task 2 created successfully.")
    return task

