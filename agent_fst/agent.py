from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

api_key = "GEMINI_API_KEY"

def morning(name : str)->str:
    """Greets the user in the morning."""
    return f"GM!! {name}, the sun is shining bright today, how can i help you "

def night(name : str)->str:
    """Greets the user at night."""
    return f"Night!! {name}, the moon is full today, how can i help you "


root_agent = Agent(
    name = "agent_fst",
    # 3. Use the defined model object instead of the model name string
    model="gemini-2.5-flash",
    description = "An agent that answers query related to Google Cloud based on google search",
    instruction = """
    first ask user their names and refer to them by their names. 
    if user says gm , greet them by using morning tool.
    if user says night , greet them by using night tool.
    """,
    tools = [morning, night, google_search],)

