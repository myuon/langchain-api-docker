from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import load_tools
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0)
tools = load_tools(["google-search", "llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.run("生命、宇宙、そして万物についての究極の疑問の答えは何ですか？")
