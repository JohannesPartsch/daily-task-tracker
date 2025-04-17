import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title):
    tasks = load_tasks()
    next_id = max([task["id"] for task in tasks], default=0) + 1
    new_task = {
        "id": next_id,
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"➕ Aufgabe hinzugefügt: [{next_id}] {title}")
