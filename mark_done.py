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
        json.dump(tasks, f, indent=2)

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print(f"🔁 Aufgabe [{task_id}] ist schon erledigt.")
            else:
                task["done"] = True
                save_tasks(tasks)
                print(f"✅ Aufgabe [{task_id}] wurde als erledigt markiert.")
            return
    print(f"❌ Keine Aufgabe mit ID [{task_id}] gefunden.")
