import json
import os
from datetime import date

TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Loads tasks from the JSON file. If the file does not exist or is invalid, 
    it returns an empty list. Handles daily resets and data migration.

    Returns:
        list: A list of tasks, each represented as a dictionary.
    """
    # Return an empty list if the tasks file does not exist
    if not os.path.exists(TASKS_FILE):
        return []

    # Attempt to load the JSON data from the file
    with open(TASKS_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    # 🔁 Automatic migration: Convert old list format to the new dictionary format
    if isinstance(data, list):
        data = {
            "last_opened": str(date.today()),
            "tasks": data
        }
        save_data(data)
        print("🔧 Old structure detected – automatically migrated.")

    # 🔄 Daily reset: Reset task completion status if the date has changed
    today_str = str(date.today())
    if data.get("last_opened") != today_str:
        for task in data.get("tasks", []):
            task["done"] = False  # Reset the 'done' status for all tasks
        data["last_opened"] = today_str
        save_data(data)
        print("🔄 New day detected – tasks have been reset.")

    # 🔀 Sort tasks by their ID before returning
    tasks = data.get("tasks", [])
    tasks.sort(key=lambda task: task.get("id", 0))  # Sort by ID (default to 0 if missing)
    return tasks

def save_tasks(tasks):
    """
    Saves the given list of tasks to the JSON file.

    Args:
        tasks (list): A list of tasks to save.
    """
    data = {
        "last_opened": str(date.today()),
        "tasks": tasks
    }
    save_data(data)

def save_data(data):
    """
    Saves the given data dictionary to the JSON file.

    Args:
        data (dict): The data to save, including metadata and tasks.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(data, f, indent=2)
