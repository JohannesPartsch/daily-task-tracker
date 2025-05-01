from ..utils.task_storage import load_tasks

def create_progress_bar(percentage, width=20):
    """
    Creates a visual progress bar.

    Args:
        percentage (float): The percentage to display (0-100).
        width (int): The width of the progress bar in characters.

    Returns:
        str: A string representing the progress bar.
    """
    filled = int(width * percentage / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"[{bar}] {percentage:.1f}%"

def show_progress():
    """
    Calculates and displays the progress of completed tasks with a visual representation.

    Returns:
        None
    """
    # Load the current list of tasks from storage
    tasks = load_tasks()

    # Check if there are any tasks
    if not tasks:
        print("📭 No tasks found.")
        return

    # Calculate statistics
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["done"])
    open_tasks = total_tasks - completed_tasks
    progress_percentage = (completed_tasks / total_tasks) * 100

    # Create the progress bar
    progress_bar = create_progress_bar(progress_percentage)

    # Display detailed progress information
    print("\n📊 Task Progress Summary")
    print("━" * 40)
    print(f"Total Tasks:     {total_tasks:3d}")
    print(f"Completed:       {completed_tasks:3d} ✅")
    print(f"Open:           {open_tasks:3d} 🔲")
    print("━" * 40)
    print(f"Progress: {progress_bar}")
    
    # Add encouraging message based on progress
    if progress_percentage == 100:
        print("\n🎉 Fantastic! All tasks completed!")
    elif progress_percentage >= 75:
        print("\n🚀 Amazing! Almost there!")
    elif progress_percentage >= 50:
        print("\n💪 Well done! More than halfway there!")
    elif progress_percentage >= 25:
        print("\n👍 Great start!")