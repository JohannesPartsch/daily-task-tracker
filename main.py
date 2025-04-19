import argparse
from add_task import add_task
from list_tasks import list_tasks
from mark_done import mark_done
from delete_task import delete_task

def main():
    parser = argparse.ArgumentParser(
        description="Daily Task Tracker CLI"
    )
    parser.add_argument(
        '--version',
        action='version',
        version='Daily Task Tracker v0.1.0'
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="ID of the task to mark as done")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()
