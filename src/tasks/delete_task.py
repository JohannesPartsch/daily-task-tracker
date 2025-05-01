from ..utils.task_storage import load_tasks, save_tasks
from ..utils.validation import validate_task_id

def delete_task(task_id):
    """
    Deletes a task by its ID after user confirmation.

    Args:
        task_id (int): The ID of the task to delete.

    Raises:
        ValueError: If the task ID is invalid or not found.
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Validate the task ID
    validate_task_id(tasks, task_id)

    # Find the task and get confirmation
    for task in tasks:
        if task["id"] == task_id:
            # Ask for confirmation before deleting
            confirm = input(f"❗ Are you sure you want to delete Task [{task_id}] '{task['title']}'? (y/n): ").lower()
            if confirm == "y":
                # Remove the task from the list
                tasks.remove(task)

                # Save the updated task list back to storage
                save_tasks(tasks)

                # Print a confirmation message
                print(f"🗑️ Task [{task_id}] has been deleted.")
            else:
                # Print a cancellation message
                print("❌ Deletion canceled.")
            return
