from ..utils.task_storage import load_tasks

def list_tasks():
    """
    Displays the list of tasks with their status, ID, and title.
    If no tasks are found, it informs the user.

    Returns:
        None
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Check if the task list is empty
    if not tasks:
        print("📭 No tasks found.")
        return

    # Print the header for the task list
    print("📋 Task List:")

    # Iterate through the tasks and display their details
    for task in tasks:
        # Determine the status icon based on the 'done' field
        status = "✅" if task["done"] else "🔲"
        # Print the task details
        print(f"{status} [{task['id']}] {task['title']}")
