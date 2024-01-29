import core
import json


def main():
    todo_list: dict[str, list[str]] = {}

    print("Simple Todo list")

    try:
        with open("todo.json", "r") as f:
            print("\nFound existing todo list!\n")
            todo_list = json.load(f)
    except FileNotFoundError:
        print("\nNo todo list was found, created new!\n")

    while True:
        print("""\nPress 'l' to show current todo list\n'A' to add a new entry\n'a' to add a task to an entry\n'D' to delete an entry\n'd' to delete a task from an entry\n'exit' to quit todo\nAnd 'Nuke' to nuke the whole list\nEnter choice: """, end="")

        user_response = input()
        print()

        match user_response:
            case "l": core.print_list(todo_list)
            case "A": core.add_entry(todo_list)
            case "a": core.add_task(todo_list)
            case "D": core.delete_entry(todo_list)
            case "d": core.delete_task(todo_list)
            case "Nuke": core.nuke_list(todo_list)
            case "exit":
                with open("todo.json", "w") as f:
                    json.dump(todo_list, f, ensure_ascii=False)
                break
            case _: print("Unknown command\n")


if __name__ == "__main__":
    main()
