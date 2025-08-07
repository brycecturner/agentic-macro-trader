import logging
from crewai import Task
from agents.research_agents import create_fed_policy_research_agent, create_banking_risk_research_agent

# Set up logging
logger = logging.getLogger("TechPodTaskLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/research_task.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def create_research_tech_company_task() -> Task:
    logger.info("Creating research task for TechPod agent.")

    tech_pod_agent = create_research_agent()

    task = Task(
        agent=tech_pod_agent,
        description=(
            "Research the top 5 technology companies by market cap (e.g., AAPL, MSFT, NVDA, GOOGL, AMZN). "
            "Summarize the most recent news, earnings reports, or macroeconomic developments affecting these firms. "
            "Your analysis should include both qualitative and quantitative insights when available."
        ),
        expected_output=(
            "A concise summary (3–5 bullet points per company) outlining key events, their market impact, and any "
            "potential signals for future price movement or volatility."
        ),
        verbose=True,
    )

    logger.info("Research task created successfully.")
    return task


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
            "A concise summary (3-5 bullet points) outlining key events, their market impact, and any "
            "potential signals for future price movement or volatility."
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
