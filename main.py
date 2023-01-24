from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


def init_agent():
    llm = OpenAI(temperature=0)
    tools = load_tools(["google-search", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
    )

    return agent


@app.route("/api/langchain", methods=["POST"])
def api_langchain():
    data = request.json
    return jsonify(agent.run(data["query"]))


if __name__ == "__main__":
    load_dotenv()

    agent = init_agent()
    app.run(port=os.environ.get("PORT", 5000))
