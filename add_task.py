from task_storage import load_tasks, save_tasks

TASKS_FILE = "tasks.json"


def add_task(title):
    tasks = load_tasks()
    used_ids = {task["id"] for task in tasks}
    next_id = 1
    while next_id in used_ids:
        next_id += 1
    new_task = {
        "id": next_id,
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"➕ Aufgabe hinzugefügt: [{next_id}] {title}")
