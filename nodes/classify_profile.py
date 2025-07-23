from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Load prompt
with open("prompts/classify.txt", "r", encoding="utf-8") as f:
    CLASSIFY_PROMPT = f.read()

# LLM config
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Node logic
def classify_profile(state: dict) -> dict:
    goal = state["goal"]
    experience = state["experience"]

    prompt = [
        HumanMessage(content=CLASSIFY_PROMPT.format(
            goal=goal,
            experience=experience
        ))
    ]

    result = llm.invoke(prompt)
    return {
        **state,
        "user_profile": result.content.strip()
    }

# Export node
classify_profile_node = RunnableLambda(classify_profile)
