# agents.py

from crewai import Agent
from tools import yt_tool  # You need to actually pass this to one of the agents
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
api_key_groq = os.getenv('GROK_API_KEY')

# Check that the key exists
if not api_key_groq:
    raise ValueError("❌ GROK_API_KEY not found in environment variables. Check your .env file.")

# Initialize Groq LLM with LLaMA 3.1
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key_groq)

# 🔹 Agent 1: Blog Researcher
blog_researcher = Agent(
    role='Blog Creator from YouTube Videos',
    goal='Get relevant video content on the topic "{topic}" from YouTube channel.',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos related to AI, Data Science, Machine Learning, and Generative AI."
    ),
    tools=[yt_tool],  # ← You were importing this but not using it
    llm=llm,
    allow_delegation=True
)

# 🔹 Agent 2: Blog Writer
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video on topic "{topic}" from a YouTube channel.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, "
        "bringing new discoveries to light in an accessible manner."
    ),
    tools=[],  # You can add summarizers, grammar tools, etc., here
    llm=llm,
    allow_delegation=False
)
