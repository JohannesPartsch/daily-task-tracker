# Daily Task Tracker

A simple command-line tool written in Python for managing daily tasks. This tool allows you to add, list, mark as done, and delete tasks, while automatically resetting task statuses daily.

## Features

- **Add Tasks**: Create new tasks with a unique ID and title.
- **List Tasks**: View all tasks with their status, ID, and title.
- **Mark Tasks as Done**: Toggle the completion status of tasks.
- **Delete Tasks**: Remove tasks by their ID after confirmation.
- **Daily Reset**: Automatically resets the completion status of tasks at the start of a new day.
- **Data Persistence**: Tasks are stored in a JSON file (`tasks.json`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JohannesPartsch/daily-task-tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd daily-task-tracker
   ```
3. Ensure you have Python 3 installed on your system.

## Usage

Run the tool using the following command:
```bash
python main.py <command> [arguments]
```

### Available Commands

- **Add a Task**:
  ```bash
  python main.py add "Task Title"
  ```
  Example:
  ```bash
  python main.py add "Buy groceries"
  ```

- **List All Tasks**:
  ```bash
  python main.py list
  ```

- **Mark a Task as Done**:
  ```bash
  python main.py done <task_id>
  ```
  Example:
  ```bash
  python main.py done 1
  ```

- **Delete a Task**:
  ```bash
  python main.py delete <task_id>
  ```
  Example:
  ```bash
  python main.py delete 1
  ```

## File Structure

- `main.py`: Entry point for the CLI application.
- `add_task.py`: Handles adding new tasks.
- `list_tasks.py`: Handles displaying tasks.
- `mark_done.py`: Handles toggling the completion status of tasks.
- `delete_task.py`: Handles deleting tasks.
- `task_storage.py`: Manages loading, saving, and resetting tasks in the JSON file.
- `tasks.json`: Stores the task data persistently.

## Example Output

### Adding a Task
```bash
➕ Task added: [1] Buy groceries
```

### Listing Tasks
```bash
📋 Task List:
🔲 [1] Buy groceries
```

### Marking a Task as Done
```bash
✅ marked as done Task [1] 'Buy groceries'
```

### Deleting a Task
```bash
❗ Are you sure you want to delete Task [1]? (y/n): y
🗑️ Task [1] has been deleted.
```
