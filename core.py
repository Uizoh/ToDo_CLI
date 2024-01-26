import utils


def is_empty(item):
    if not item:
        return True
    else:
        return False


def print_list(todo_list: dict):

    if is_empty(todo_list):
        print("Looks like your todo list is empty...\n")
        return

    for keys, values in todo_list.items():
        print(f"{keys}")

        for v in values:
            print(f"- {v}")
    print()


def add_entry(todo_list: dict):

    print("Enter new entry name: ", end="")
    entry_name = input()

    if entry_name in todo_list:
        print("This entry already exists!\n")
        return

    todo_list[entry_name] = []


def add_task(todo_list: dict):

    if is_empty(todo_list):
        print("Please add an entry first to add tasks. Entries are titles for specific todo list\n")
        return

    print("Select an entry to add a task: \n")

    temp_list = utils.create_indexed_list(todo_list)
    utils.print_indexed_list(temp_list)

    print("Enter number for the entry: ", end="")
    response = int(input())
    response -= 1

    if response < 0 or response >= len(temp_list):
        print("Selected number does not exist in entry list!\n")
        return

    selected_entry: str = temp_list[response]

    print("Enter task name: ", end="")
    task_name = input()

    todo_list[selected_entry].append(task_name)


def delete_entry(todo_list: dict):

    if is_empty(todo_list):
        print("There are no enties to delete from\n")
        return

    print("Select an entry to delete: \n")

    temp_list = utils.create_indexed_list(todo_list)
    utils.print_indexed_list(temp_list)

    print("Enter the entry number you want to delete: ", end="")
    response = int(input())
    response -= 1

    if response < 0 or response >= len(temp_list):
        print("Entered number does not exist in the list!\n")
        return

    selected_entry: str = temp_list[response]

    todo_list.pop(selected_entry)
    print()


def delete_task(todo_list: dict):

    if is_empty(todo_list):
        print("There are no enties to delete from\n")
        return

    print("Select an entry to delete a task from: \n")

    temp_list = utils.create_indexed_list(todo_list)
    utils.print_indexed_list(temp_list)

    print("Enter the number of the entry: ", end="")
    response = int(input())
    response -= 1

    if response < 0 or response >= len(temp_list):
        print("Selected number does not exist in entry list!\n")
        return

    selected_entry: str = temp_list[response]

    if is_empty(todo_list[selected_entry]):
        print("This entry does not have any task\n")
        return

    print("Select a task to delete from the list: \n")
    for i in range(len(todo_list[selected_entry])):
        print(f"{i+1}. {todo_list[selected_entry][i]}")

    print("Enter the task number to delete: ", end="")
    response = int(input())
    response -= 1

    if todo_list[selected_entry][response] is None:
        print("Selected number does not exist in the task list!\n")
        return

    todo_list[selected_entry].pop(response)
    print()


def nuke_list(todo_list: dict):
    print("Are you sure you want to delete the whole ToDo list? y/n")
    response = input()

    if response == 'y':
        todo_list.clear()
        print()
    else:
        print("List deletion cancled\n")
