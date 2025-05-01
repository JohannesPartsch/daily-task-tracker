from ..utils.task_storage import load_tasks, save_tasks
from ..utils.validation import validate_task_title

def add_task(title):
    """
    Adds a new task to the task list.

    Args:
        title (str): The title of the task to be added.

    Raises:
        ValueError: If the title is invalid.
    """
    # Validate the title
    validate_task_title(title)

    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Collect all used IDs to ensure uniqueness
    used_ids = {task["id"] for task in tasks}

    # Find the next available ID
    next_id = 1
    while next_id in used_ids:
        next_id += 1

    # Create a new task dictionary
    new_task = {
        "id": next_id,
        "title": title.strip(),  # Remove leading/trailing whitespace
        "done": False  # New tasks are not completed by default
    }

    # Add the new task to the list
    tasks.append(new_task)

    # Save the updated task list back to storage
    save_tasks(tasks)

    # Print a confirmation message
    print(f"➕ Task added: [{next_id}] {title}")
