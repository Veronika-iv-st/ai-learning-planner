## 🧠 Personalized Learning Path Agent

### 🎯 Overview

This project implements an intelligent agent that generates a **personalized 5-week learning path**, tailored to the user's goals, previous experience, and profile. It uses **LangChain 0.3+**, **LangGraph**, and **LLM models** to guide the construction of the plan through a conversational interface.

The agent starts with a short interaction to understand what the user wants to learn and their current experience level. Based on this:

* It classifies their educational or professional profile.
* It generates a structured week-by-week study plan.
* It adapts the content to the detected level.

This flow is designed to scale and includes LangGraph nodes that can be extended, modified, or connected to future APIs.

---

### 🛠 Technologies Used

* [Python 3.11+](https://www.python.org/)
* [LangChain Core](https://python.langchain.com/)
* [LangGraph](https://github.com/langchain-ai/langgraph)
* [OpenAI API](https://platform.openai.com/)
* [dotenv](https://pypi.org/project/python-dotenv/) for environment variables

---

### 📂 Project Structure

```bash
learning_path_agent/
├── graph.py                      # Main LangGraph flow
├── nodes/
│   ├── ask_user_input.py         # Conversational entry node
│   ├── classify_profile.py       # Classifies user profile
│   └── generate_plan.py          # Generates the learning plan
├── prompts/
│   ├── classify.txt              # Prompt for profile classification
│   └── generate.txt              # Prompt to generate the complete plan
├── .env                          # Contains your OpenAI API key
└── README.md                     # Project documentation
```

---

### 🔄 Agent Flow (LangGraph)

```text
ask_user_input ➔ classify_profile ➔ generate_plan
```

1. `ask_user_input.py` asks the user:

   * What they want to learn (`goal`)
   * Their current experience (`experience`)

2. `classify_profile.py` processes this information and classifies the user as "Beginner", "Career Switcher", "Technical", etc.

3. `generate_plan.py` builds a week-by-week learning plan adapted to the user's profile and objectives.

---

### 📘 Example Usage

```bash
python graph.py
```

Expected output:

```
👋 Hello! I’m your learning path assistant.

🧠 What would you like to learn?
> I want to learn artificial intelligence for marketing

📚 What is your current experience level?
> I’m a marketing expert but I’ve never programmed

🔹 Profile detected: Career Switcher

📚 Personalized learning plan:
Week 1: Introduction to AI
Week 2: Python basics
...
```

---

### 📌 Possible Future Extensions

* Export the plan to PDF or HTML
* Integration with real course APIs (Coursera, Udemy...)
* Learning style selector node (visual, hands-on, self-paced)
* Web interface using FastAPI or Gradio
* History of saved plans per user

---

### 👤 Author

Veronika Ivanova · Artificial Intelligence Architect
