import core
from utils import Colour as c
import json


def main():
    todo_list: dict[str, list[str]] = {}

    print(f"{c.HIGHLIGHT} Simple Todo list {c.RESET}")

    try:
        with open("todo.json", "r") as f:
            print(f"\n{c.GREEN}Found existing todo list!{
                  c.RESET}\n")
            todo_list = json.load(f)
    except FileNotFoundError:
        print(f"\n{c.ORANGE}No todo list was found, created new!{
              c.RESET}\n")

    while True:
        print(f"{c.CYAN}\nPress 'l' to show current todo list\n'A' to add a new title\n'a' to add a task to an title\n'D' to delete an title\n'd' to delete a task from an title\n'clear' to clear the whole list\nAnd 'exit' to quit todo{
              c.RESET}\n\nEnter choice: ", end="")

        user_response = input()
        print()

        match user_response:
            case "l": core.print_list(todo_list)
            case "A": core.add_title(todo_list)
            case "a": core.add_task(todo_list)
            case "D": core.delete_title(todo_list)
            case "d": core.delete_task(todo_list)
            case "clear": core.clear_list(todo_list)
            case "exit":
                with open("todo.json", "w") as f:
                    json.dump(todo_list, f, ensure_ascii=False)
                break
            case _: print(f"{c.RED}Unknown command{c.RESET}\n")


if __name__ == "__main__":
    main()
