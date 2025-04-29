from ..utils.task_storage import load_tasks, save_tasks

def delete_task(task_id):
    """
    Deletes a task by its ID after user confirmation.

    Args:
        task_id (int): The ID of the task to delete.
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Iterate through the tasks to find the one with the matching ID
    for task in tasks:
        if task["id"] == task_id:
            # Ask the user for confirmation before deleting the task
            confirm = input(f"❗ Are you sure you want to delete Task [{task_id}]? (y/n): ").lower()
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

    # If no task with the given ID is found, print an error message
    print(f"❌ No task found with ID [{task_id}].")
