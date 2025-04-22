from task_storage import load_tasks

def show_progress():
    """
    Calculates and displays the progress of completed tasks.

    Returns:
        None
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Check if there are any tasks
    if not tasks:
        print("📭 No tasks found.")
        return

    # Calculate the number of completed and total tasks
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["done"])

    # Calculate the completion percentage
    progress_percentage = (completed_tasks / total_tasks) * 100

    # Display the progress
    print(f"📊 Progress: {completed_tasks}/{total_tasks} tasks completed ({progress_percentage:.0f}%)")