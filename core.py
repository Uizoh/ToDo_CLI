import utils
from utils import Colour as c


def is_empty(item):
    if not item:
        return True
    else:
        return False


def print_list(todo_list: dict):

    if is_empty(todo_list):
        print(f"{c.ORANGE}Looks like your todo list is empty...{c.RESET}\n")
        return

    print(f"Here is your todo list:{c.BLUE}")
    for keys, values in todo_list.items():
        print(f"{keys}")

        for v in values:
            print(f"- {v}")
    print(c.RESET)


def add_title(todo_list: dict):

    print("Enter new title name: ", end="")
    title_name = input()

    if title_name in todo_list:
        print(f"{c.RED}This title already exists!{c.RESET}\n")
        return

    todo_list[title_name] = []
    print(f"{c.GREEN}Title added successfully{c.RESET}")


def add_task(todo_list: dict):

    if is_empty(todo_list):
        print(f"{c.RED}Please add an title first to add tasks. These are headers for todo lists{
              c.RESET}\n")
        return

    print(f"{c.CYAN}Select an title to add a task: {c.RESET}\n")

    temp_list = utils.create_indexed_list(todo_list)
    utils.print_indexed_list(temp_list)

    print("Enter number for the title: ", end="")
    response = int(input())
    response -= 1

    if response < 0 or response >= len(temp_list):
        print(f"{c.RED}Selected number does not exist in title list!{c.RESET}\n")
        return

    selected_title: str = temp_list[response]

    print("Enter task name: ", end="")
    task_name = input()

    todo_list[selected_title].append(task_name)
    print(f"{c.GREEN}\nTask was successfully added{c.RESET}")


def delete_title(todo_list: dict):

    if is_empty(todo_list):
        print(f"{c.RED}\nThere are no enties to delete from{c.RESET}\n")
        return

    print(f"{c.CYAN}Select an title to delete: \n{c.RESET}")

    temp_list = utils.create_indexed_list(todo_list)
    utils.print_indexed_list(temp_list)

    print("Enter the title number you want to delete: ", end="")
    response = int(input())
    response -= 1

    if response < 0 or response >= len(temp_list):
        print(f"{c.RED}\nEntered number does not exist in the list{c.RESET}!\n")
        return

    selected_title: str = temp_list[response]

    todo_list.pop(selected_title)
    print(f"{c.HIGHLIGHT}{
          c.ORANGE}\nTitle was deleted along with it's tasks{c.RESET}")


def delete_task(todo_list: dict):

    if is_empty(todo_list):
        print(f"{c.RED}There are no enties to delete from{c.RESET}\n")
        return

    print(f"{c.CYAN}Select an title to delete a task from: \n{c.RESET}")

    temp_list = utils.create_indexed_list(todo_list)
    utils.print_indexed_list(temp_list)

    print("Enter the number of the title: ", end="")
    response = int(input())
    response -= 1

    if response < 0 or response >= len(temp_list):
        print(f"{c.RED}Selected number does not exist in title list!{c.RESET}\n")
        return

    selected_title: str = temp_list[response]

    if is_empty(todo_list[selected_title]):
        print(f"{c.RED}This title does not have any task{c.RESET}\n")
        return

    print(f"{c.CYAN}Select a task to delete from the list: \n{c.RESET}")

    print(c.BLUE, end="")

    for i in range(len(todo_list[selected_title])):
        print(f"{i+1}. {todo_list[selected_title][i]}")

    print(c.RESET, end="")

    print("Enter the task number to delete: ", end="")
    response = int(input())
    response -= 1

    if todo_list[selected_title][response] is None:
        print(f"{c.RED}\nSelected number does not exist in the task list!{c.RESET}\n")
        return

    todo_list[selected_title].pop(response)
    print(f"{c.HIGHLIGHT}{c.ORANGE}Selected task was deleted successfully")


def clear_list(todo_list: dict):
    print(f"{c.CYAN}Are you sure you want to delete the whole ToDo list? y/n: {c.RESET}", end="")
    response = input()

    if response == 'y':
        todo_list.clear()
        print(f"{c.HIGHLIGHT}{c.RED}\nTodo list has been cleared! {c.RESET}")
    else:
        print(f"{c.RED}List deletion cancled{c.RESET}\n")
