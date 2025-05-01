def validate_task_id(tasks, task_id):
    """
    Validates that a task ID exists in the task list.

    Args:
        tasks (list): The list of tasks to check.
        task_id (int): The ID to validate.

    Raises:
        ValueError: If the task ID is invalid or not found.
    """
    if task_id < 1:
        raise ValueError("Task ID must be greater than 0.")
    
    if not any(task["id"] == task_id for task in tasks):
        raise ValueError(f"No task found with ID [{task_id}].")

def validate_task_title(title):
    """
    Validates the task title.

    Args:
        title (str): The title to validate.

    Raises:
        ValueError: If the title is invalid.
    """
    if not title:
        raise ValueError("Title cannot be empty.")
    if len(title) > 100:
        raise ValueError("Title cannot be longer than 100 characters.")
    if title.isspace():
        raise ValueError("Title cannot contain only whitespace.")