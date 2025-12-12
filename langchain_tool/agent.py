import os
import sys
from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool 
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from litellm import completion
from dotenv import load_dotenv

# Loads GROQ_API_KEY from the .env file
load_dotenv()

os.environ['GROQ_API_KEY']

root_agent = Agent(
    name="lanchgain_tool_agent",
    model="groq/llama-3.1-8b-instant", 
    description="Answers questions using Wikipedia.",
    instruction="""Research the topic suggested by the user.
    Share the information you have found with the user.""",
    tools = [
        LangchainTool(
            tool=WikipediaQueryRun(
                api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
)

print(f"Agent '{root_agent.name}' initialized successfully using Groq/Llama 3.1.")