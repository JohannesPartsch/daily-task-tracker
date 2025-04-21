from task_storage import load_tasks, save_tasks

TASKS_FILE = "tasks.json"

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            status = "✅ erledigt" if task["done"] else "↩️ wieder unerledigt"
            save_tasks(tasks)
            print(f"{status} Aufgabe [{task_id}] '{task['title']}'")
            return
    print(f"❌ Keine Aufgabe mit ID [{task_id}] gefunden.")
