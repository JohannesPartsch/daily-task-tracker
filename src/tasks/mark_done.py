from ..utils.task_storage import load_tasks, save_tasks
from ..utils.validation import validate_task_id

def mark_done(task_id):
    """
    Toggles the completion status of a task by its ID.

    Args:
        task_id (int): The ID of the task to toggle.

    Raises:
        ValueError: If the task ID is invalid or not found.
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Validate the task ID
    validate_task_id(tasks, task_id)

    # Find and update the task
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
