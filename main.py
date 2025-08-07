import os
from dotenv import load_dotenv
import asyncio
# import nest_asyncio
from crew.create_crew import create_crew
from crew.run_parallel_crews import run_parallel_crews

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# Entry point
if __name__ == "__main__":
    #nest_asyncio.apply()  # Useful for notebooks or environments that complain about running loops

    fed_result, bank_result = asyncio.run(run_parallel_crews())

    print("\n📰 Fed Research Output:\n", fed_result)
    print("\n🏦 Banking Risk Output:\n", bank_result)
