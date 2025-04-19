from task_storage import load_tasks, save_tasks

def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            confirm = input(f"❗ Aufgabe [{task_id}] wirklich löschen? (j/n): ").lower()
            if confirm == "j":
                tasks.remove(task)
                save_tasks(tasks)
                print(f"🗑️ Aufgabe [{task_id}] wurde gelöscht.")
            else:
                print("❌ Abgebrochen.")
            return
    print(f"❌ Keine Aufgabe mit ID [{task_id}] gefunden.")
