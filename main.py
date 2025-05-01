import argparse
import sys
from src.tasks.add_task import add_task
from src.tasks.list_tasks import list_tasks
from src.tasks.mark_done import mark_done
from src.tasks.delete_task import delete_task
from src.tasks.progress import show_progress

# Command mapping dictionary
COMMANDS = {
    "add": {
        "function": add_task,
        "help": "Add a new task",
        "args": [("title", {"help": "Title of the task"})],
    },
    "list": {
        "function": list_tasks,
        "help": "List all tasks",
        "args": [],
    },
    "done": {
        "function": mark_done,
        "help": "Mark a task as done",
        "args": [("id", {"type": int, "help": "ID of the task to mark as done"})],
    },
    "delete": {
        "function": delete_task,
        "help": "Delete a task",
        "args": [("id", {"type": int, "help": "ID of the task to delete"})],
    },
    "progress": {
        "function": show_progress,
        "help": "Show progress of completed tasks",
        "args": [],
    },
}

def main():
    """
    Entry point for the Daily Task Tracker CLI application.
    This function sets up the command-line interface and handles user commands.
    """
    try:
        # Initialize the argument parser
        parser = argparse.ArgumentParser(
            description="Daily Task Tracker CLI"
        )
        
        # Add a version flag
        parser.add_argument(
            '--version',
            action='version',
            version='Daily Task Tracker v0.2.0'  # Updated to reflect implemented features
        )
        
        # Create subparsers for different commands
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Dynamically add commands from the COMMANDS dictionary
        for cmd_name, cmd_info in COMMANDS.items():
            cmd_parser = subparsers.add_parser(cmd_name, help=cmd_info["help"])
            for arg_name, arg_props in cmd_info["args"]:
                cmd_parser.add_argument(arg_name, **arg_props)

        # Parse the command-line arguments
        args = parser.parse_args()

        # Show help if no command is provided
        if not args.command:
            parser.print_help()
            return

        # Get the command function and execute it with the appropriate arguments
        cmd_info = COMMANDS[args.command]
        cmd_func = cmd_info["function"]
        
        # Extract the required arguments for the function
        cmd_args = [getattr(args, arg_name) for arg_name, _ in cmd_info["args"]]
        
        # Execute the command
        cmd_func(*cmd_args)

    except KeyboardInterrupt:
        print("\n👋 Program terminated.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
