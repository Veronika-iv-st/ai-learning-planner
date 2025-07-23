from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Load prompt
with open("prompts/generate.txt", "r", encoding="utf-8") as f:
    GENERATE_PROMPT = f.read()

# LLM config
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

# Node logic
def generate_learning_plan(state: dict) -> dict:
    goal = state["goal"]
    experience = state["experience"]
    profile = state["user_profile"]

    prompt = [
        HumanMessage(content=GENERATE_PROMPT.format(
            goal=goal,
            experience=experience,
            profile=profile
        ))
    ]

    result = llm.invoke(prompt)
    return {
        **state,
        "learning_plan": result.content.strip()
    }

# Export node
generate_plan_node = RunnableLambda(generate_learning_plan)
