import json
import os
from datetime import date
from pathlib import Path

TASKS_FILE = "data/tasks.json"

def ensure_data_dir():
    """
    Ensures that the data directory exists.
    Creates it if it doesn't exist.
    """
    data_dir = os.path.dirname(TASKS_FILE)
    Path(data_dir).mkdir(parents=True, exist_ok=True)

def load_tasks():
    """
    Loads tasks from the JSON file. If the file does not exist or is invalid, 
    it returns an empty list. Handles daily resets and data migration.

    Returns:
        list: A list of tasks, each represented as a dictionary.
    
    Raises:
        OSError: If there's a filesystem-related error.
    """
    try:
        ensure_data_dir()
        
        # Return an empty list if the tasks file does not exist
        if not os.path.exists(TASKS_FILE):
            return []

        # Attempt to load the JSON data from the file
        with open(TASKS_FILE, "r", encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"⚠️ Warning: Corrupted tasks.json file. Creating new empty list. ({str(e)})")
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

    except OSError as e:
        print(f"❌ Error loading tasks: {str(e)}")
        raise

def save_tasks(tasks):
    """
    Saves the given list of tasks to the JSON file.

    Args:
        tasks (list): A list of tasks to save.
    
    Raises:
        OSError: If there's a filesystem-related error.
        TypeError: If the tasks cannot be serialized to JSON.
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
    
    Raises:
        OSError: If there's a filesystem-related error.
        TypeError: If the data cannot be serialized to JSON.
    """
    try:
        ensure_data_dir()
        
        # Create a backup of the existing file if it exists
        if os.path.exists(TASKS_FILE):
            backup_file = f"{TASKS_FILE}.bak"
            try:
                os.replace(TASKS_FILE, backup_file)
            except OSError as e:
                print(f"⚠️ Warning: Could not create backup: {str(e)}")

        # Save the new data
        with open(TASKS_FILE, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    except (OSError, TypeError) as e:
        print(f"❌ Error saving tasks: {str(e)}")
        # Try to restore from backup if save failed
        if os.path.exists(f"{TASKS_FILE}.bak"):
            try:
                os.replace(f"{TASKS_FILE}.bak", TASKS_FILE)
                print("✅ Backup restored.")
            except OSError:
                print("❌ Could not restore backup.")
        raise
