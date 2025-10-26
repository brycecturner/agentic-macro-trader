# tools/research_tools.py
import logging

from crewai_tools import (
    SerperDevTool,
    # ScrapeWebsiteTool,
    # PDFSearchTool,
    # JsonFormattingTool,
    # PythonTool
)

logger = logging.getLogger(__name__)

def research_tools():
    """
    Returns a standard set of tools for macro/multi-strategy research agents.

    Includes:
    - Web search
    - Web scraping
    - PDF parsing
    - Python for quick calculations
    - Structured JSON output formatting
    """
    
    logger.info("Initializing standard research tools for agents...")

    tools = [
        SerperDevTool(),         # Search the web (via Serper API)
        # ScrapeWebsiteTool(),   # Pull text from URLs
        # PDFSearchTool(),       # Extract info from PDF reports
        # PythonTool(),          # Do lightweight calcs
        # JsonFormattingTool(),  # Output in JSON for downstream crews
    ]

    logger.info(f"Loaded {len(tools)} research tools: {[tool.__class__.__name__ for tool in tools]}")
    return tools

def serper_logic_for_query():
    return (
        "Use the Serper tool to search the web for relevant information. Formulate your query based on the research topic and use the tool to gather up-to-date data. Analyze the search results and extract key insights to inform your research. When invoking the SerperDevTool, pass only simple text strings."
    )
