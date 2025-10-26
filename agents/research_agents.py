import logging
from crewai import Agent
from tools.research_tools import research_tools
from utils.utils import get_current_date_for_prompting

# Set up logging
logger = logging.getLogger("research_agent")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/research_agent.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def create_banking_risk_research_agent() -> Agent:
    logger.info("Creating banking system fragility research agent...")

    agent = Agent(
        role="Banking System Risk Analyst",
        goal=(
            "Monitor and evaluate the stability of the banking sector by identifying early warning signs "
            "of systemic risk such as declining bank reserves, rising loan defaults, interbank stress, "
            "or liquidity shortages."
        ),
        backstory=(
            "You are a macroeconomic researcher at a hedge fund tasked with identifying risks in the banking sector. "
            "You specialize in analyzing regulatory filings, central bank reports, and market data to anticipate "
            "systemic financial stress. Your insights feed directly into portfolio risk controls and hedging strategies."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),  # Optional, add more if needed
    )

    logger.info("Banking system risk research agent created successfully.")
    return agent

def create_fed_policy_research_agent() -> Agent:
    logger.info("Creating Federal Reserve monetary policy research agent...")

    agent = Agent(
        role="Federal Reserve Policy Analyst",
        goal=(
            "Track, interpret, and forecast the Federal Reserve’s monetary policy decisions, including interest rate changes, "
            "quantitative tightening or easing, balance sheet positioning, and public communications from FOMC members."
        ),
        backstory=(
            "You are a macroeconomic researcher at a hedge fund focused exclusively on central bank policy. "
            "You analyze FOMC statements, meeting minutes, press conferences, and speeches from Fed officials. "
            "You combine this with market-based indicators such as the Fed Funds futures curve, inflation breakevens, "
            "and Treasury yields to forecast likely policy shifts. Your insights help inform positioning across rates, FX, and equities."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),  # Extend with other document or data tools if needed
    )

    logger.info("Federal Reserve policy research agent created successfully.")
    return agent

def create_global_capital_flows_research_agent() -> Agent:
    logger.info("Creating Global Capital Flows research agent...")

    agent = Agent(
        role="Global Capital Flow Analyst",
        goal=(
            "Track and interpret international capital movements across regions and asset classes to assess cross-border investment trends and their impact on markets."
        ),
        backstory=(
            "You are a macro researcher specializing in global capital allocation. "
            "You monitor international investment flows, portfolio flows data (e.g., TIC, EPFR), FX reserves, sovereign wealth fund activity, and institutional positioning. "
            "Your insights help anticipate macro imbalances, currency volatility, and capital flight or inflows that affect EM and DM assets."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),
    )

    logger.info("Global Capital Flows agent created successfully.")
    return agent

def create_fiscal_policy_research_agent() -> Agent:
    logger.info("Creating Fiscal Policy and Sovereign Balance Sheet research agent...")

    agent = Agent(
        role="Fiscal Policy Analyst",
        goal=(
            "Assess the fiscal stance of major governments and the sustainability of sovereign balance sheets to identify macro risks and investment opportunities."
        ),
        backstory=(
            "You specialize in analyzing government budgets, debt issuance, fiscal multipliers, and sovereign risk indicators. "
            "You track fiscal stimulus, tax policy, deficit trends, and debt servicing capacity across major and emerging economies. "
            "Your forecasts inform decisions related to bond markets, credit spreads, and FX risk."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),
    )

    logger.info("Fiscal Policy agent created successfully.")
    return agent

def create_macro_growth_research_agent() -> Agent:
    logger.info("Creating Macro Growth & Employment Indicators agent...")

    agent = Agent(
        role="Macro Growth Analyst",
        goal=(
            "Track GDP, employment, consumption, and productivity trends across global economies to assess cyclical momentum and recession risk."
        ),
        backstory=(
            "You are an economist at a global macro hedge fund. "
            "You analyze high-frequency economic indicators (e.g., nonfarm payrolls, ISM, retail sales, PMI), as well as GDP data, to track real-time shifts in growth. "
            "Your insights help determine positioning in risk assets, rates, and FX."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),
    )

    logger.info("Macro Growth agent created successfully.")
    return agent

def create_macro_inflation_research_agent() -> Agent:
    logger.info("Creating Macro Inflation & Wages Indicators agent...")

    agent = Agent(
        role="Inflation Dynamics Analyst",
        goal=(
            "Monitor inflation trends, wage growth, and pricing power to understand underlying inflationary pressures in developed and emerging economies."
        ),
        backstory=(
            "You study CPI, PCE, wage reports, supply chain disruptions, and pricing surveys to form a detailed view of inflation dynamics. "
            "You cross-reference central bank communications and market-based inflation expectations to assess inflation persistence and policy response."
            f"{get_current_date_for_prompting()}"
        ),
        allow_delegation=False,
        verbose=True,
        tools=research_tools(),
    )

    logger.info("Macro Inflation agent created successfully.")
    return agent
