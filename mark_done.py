from task_storage import load_tasks, save_tasks

TASKS_FILE = "tasks.json"

def mark_done(task_id):
    """
    Toggles the completion status of a task by its ID.

    Args:
        task_id (int): The ID of the task to toggle.
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Iterate through the tasks to find the one with the matching ID
    for task in tasks:
        if task["id"] == task_id:
            # Toggle the 'done' status of the task
            task["done"] = not task["done"]

            # Determine the new status message
            status = "✅ marked as done" if task["done"] else "↩️ marked as not done"

            # Save the updated task list back to storage
            save_tasks(tasks)

            # Print a confirmation message
            print(f"{status} Task [{task_id}] '{task['title']}'")
            return

    # If no task with the given ID is found, print an error message
    print(f"❌ No task found with ID [{task_id}].")
