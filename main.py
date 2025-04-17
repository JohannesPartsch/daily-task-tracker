import argparse

def main():
    parser = argparse.ArgumentParser(description="Daily Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    subparsers.add_parser("add", help="Add a new task")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Done command
    subparsers.add_parser("done", help="Mark a task as done")

    args = parser.parse_args()

    if args.command == "add":
        print("➕ Neue Aufgabe hinzufügen (noch nicht implementiert)")
    elif args.command == "list":
        print("📋 Aufgaben auflisten (noch nicht implementiert)")
    elif args.command == "done":
        print("✅ Aufgabe als erledigt markieren (noch nicht implementiert)")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
