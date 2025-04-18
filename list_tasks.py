from task_storage import load_tasks

TASKS_FILE = "tasks.json"

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Keine Aufgaben gefunden.")
        return

    print("📋 Aufgabenliste:")
    for task in tasks:
        status = "✅" if task["done"] else "🔲"
        print(f"{status} [{task['id']}] {task['title']}")
