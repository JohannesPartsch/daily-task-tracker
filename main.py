import argparse
from add_task import add_task
from list_tasks import list_tasks
from mark_done import mark_done
from delete_task import delete_task

def main():
    """
    Entry point for the Daily Task Tracker CLI application.
    This function sets up the command-line interface and handles user commands.
    """
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="Daily Task Tracker CLI"
    )
    
    # Add a version flag
    parser.add_argument(
        '--version',
        action='version',
        version='Daily Task Tracker v0.1.0'
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command: Allows the user to add a new task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")

    # List command: Displays all tasks
    subparsers.add_parser("list", help="List all tasks")

    # Done command: Marks a task as completed
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="ID of the task to mark as done")

    # Delete command: Deletes a task by its ID
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Handle the commands based on user input
    if args.command == "add":
        add_task(args.title)  # Call the function to add a task
    elif args.command == "list":
        list_tasks()  # Call the function to list all tasks
    elif args.command == "done":
        mark_done(args.id)  # Call the function to mark a task as done
    elif args.command == "delete":
        delete_task(args.id)  # Call the function to delete a task
    else:
        parser.print_help()  # Show help message if no valid command is provided


if __name__ == "__main__":
    main()
