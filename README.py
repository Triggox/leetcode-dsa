import os
from datetime import datetime

# Define your folder structure (adjust as needed)
TOPICS = ["Arrays", "DP", "Greedy", "Trees", "Graphs", "Strings"]

def collect_problems():
    logs = []
    for topic in TOPICS:
        topic_path = os.path.join(".", topic)
        if os.path.exists(topic_path):
            for file in os.listdir(topic_path):
                if file.endswith(".cpp") or file.endswith(".py") or file.endswith(".java"):
                    logs.append({
                        "date": datetime.today().strftime("%Y-%m-%d"),
                        "problem": os.path.splitext(file)[0],
                        "topic": topic,
                        "status": "✅"
                    })
    return logs

def generate_table(logs):
    table = "| Date | Problem | Topic | Status |\n"
    table += "|------|---------|--------|--------|\n"
    for log in logs:
        table += f"| {log['date']} | {log['problem']} | {log['topic']} | {log['status']} |\n"
    return table

def update_readme(logs):
    with open("README.md", "w") as f:
        f.write("# 🧠 LeetCode Progress Tracker\n\n")
        f.write("This README auto-updates based on the problems stored in this repo.\n\n")
        f.write(generate_table(logs))

if __name__ == "__main__":
    logs = collect_problems()
    update_readme(logs)
    print("README updated with current LeetCode problem logs.")
