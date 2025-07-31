import os
from dotenv import load_dotenv
from crew.create_crew import create_crew

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    crew = create_crew()

    result = crew.kickoff()

    print("\n=== FINAL OUTPUT ===\n")
    print(result)
