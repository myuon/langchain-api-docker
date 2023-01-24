from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from waitress import serve
import logging
from flask import request
from flask import Flask
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
)

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


def init_agent():
    llm = OpenAI(temperature=0)
    tools = load_tools(["google-search", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=False,
    )

    return agent


@app.route("/api/langchain", methods=["POST"])
def api_langchain():
    data = request.json
    return jsonify({"result": agent.run(data["query"])})


if __name__ == "__main__":
    load_dotenv()

    agent = init_agent()
    serve(app, host="0.0.0.0", port=os.environ.get("PORT", 5000))
