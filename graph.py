from langgraph.graph import StateGraph
from typing import TypedDict
from nodes.ask_user_input import ask_user_input_node
from nodes.classify_profile import classify_profile_node
from nodes.generate_plan import generate_plan_node
import datetime
import re

# Updated state schema
class LearningState(TypedDict):
    goal: str
    experience: str
    user_profile: str
    learning_plan: str

# Build the graph
builder = StateGraph(LearningState)
builder.add_node("ask_user_input", ask_user_input_node)
builder.add_node("classify_profile", classify_profile_node)
builder.add_node("generate_plan", generate_plan_node)

builder.set_entry_point("ask_user_input")
builder.add_edge("ask_user_input", "classify_profile")
builder.add_edge("classify_profile", "generate_plan")
builder.set_finish_point("generate_plan")

graph = builder.compile()

# Run
if __name__ == "__main__":
    result = graph.invoke({})  # Now we don't pass anything manually

    print("\n✅ Profile detected:")
    print(result["user_profile"])
    print("\n📘 Personalized learning plan:")
    print(result["learning_plan"])

    # offer to save
    save = input("\n Do you want to save this learning plan as a .txt file? (y/n): ").strip().lower()
    if save == "y":
        goal = result["goal"]
        goal_snippet = re.sub(r'\W+', '_', goal.strip())[:20]
        today = datetime.date.today().isoformat()
        filename = f"{goal_snippet}_{today}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"User Profile: {result['user_profile']}\n\n")
            f.write("Personalized Learning Plan:\n")
            f.write(result["learning_plan"])

        print(f"Learning plan saved as '{filename}'")