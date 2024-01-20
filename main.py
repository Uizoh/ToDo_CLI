from typing import Dict, List
import mod


def main():
    todo_list: Dict[str, List[str]] = {}

    print("Simple Todo list")
    print("Press 'l' to show current todo list\n'A' to add a new entry\n \
    'a' to add a task to an entry\n'D' to delete an entry\n \
    'd' to delete a task from an entry\nAnd 'Nuke' to nuke the whole list"
          )

    user_response = input()

    match user_response:
        case "l": mod.print_list(todo_list)
        case "A": mod.add_entry(todo_list)
        case "a": mod.add_task(todo_list)
        case "D": mod.delete_entry(todo_list)
        case "d": mod.delete_task(todo_list)


if __name__ == "__main__":
    main()
