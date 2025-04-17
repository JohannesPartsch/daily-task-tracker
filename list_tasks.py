import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Keine Aufgaben gefunden.")
        return

    print("📋 Aufgabenliste:")
    for task in tasks:
        status = "✅" if task["done"] else "🔲"
        print(f"{status} [{task['id']}] {task['title']}")
