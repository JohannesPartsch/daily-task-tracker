from task_storage import load_tasks, save_tasks

TASKS_FILE = "tasks.json"

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
