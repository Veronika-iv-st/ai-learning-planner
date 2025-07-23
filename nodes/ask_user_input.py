from langchain_core.runnables import RunnableLambda

def ask_user_input(_: dict) -> dict:
    print("\n👋 Hello! I’m your learning path assistant.\n")

    goal = input("🧠 What would you like to learn? (e.g., AI for marketing):\n> ")
    experience = input("\n📚 What is your current experience level or background?\n> ")

    return {
        "goal": goal.strip(),
        "experience": experience.strip()
    }

ask_user_input_node = RunnableLambda(ask_user_input)
