from typing import Dict


def print_list(todo_list: Dict):
    for keys, values in todo_list.items():
        print(f"{keys}")

        for v in values:
            print(f"- {v}")


def add_entry(todo_list: Dict):

    print("Enter new entry name: ", end="")
    entry_name = input()

    if todo_list.__contains__(entry_name):
        print("This entry already exists!\n")
        return

    todo_list[entry_name] = []


def create_temp_list(todo_list: Dict) -> Dict:

    temp_list: Dict[int, str] = {}

    for k in todo_list.keys():
        i = 1
        temp_list[i] = k
        i += 1

    return temp_list


def print_temp_list(temp_list: Dict):
    # To present the list with index
    for k, v in temp_list.items():
        print(f"{k}. {v}")


def add_task(todo_list: Dict):

    print("Select an entry to add a task: \n")

    temp_list = create_temp_list(todo_list)
    print_temp_list(temp_list)

    print("Enter number for the entry: ", end="")
    response = int(input())

    if not temp_list.__contains__(response):
        print("Selected number does not exist in entry list!\n")
        return

    selected_entry: str = temp_list[response]

    print("Enter task name: ", end="")
    task_name = input()

    todo_list[selected_entry].append(task_name)


def delete_entry(todo_list: Dict):

    print("Select an entry to delete: \n")

    temp_list = create_temp_list(todo_list)
    print_temp_list(temp_list)

    print("Enter the entry number you want to delete: ", end="")
    response = input()

    if not temp_list.__contains__(response):
        print("Entered number does not exist in the list!\n")
        return

    selected_entry: str = temp_list[response]

    todo_list.pop(selected_entry)


def delete_task(todo_list: Dict):

    print("Select an entry to delete a task from: \n")

    temp_list = create_temp_list(todo_list)
    print_temp_list(temp_list)

    print("Enter the number of the entry: ", end="")
    response = int(input())

    if not temp_list.__contains__(response):
        print("Selected number does not exist in entry list!\n")
        return

    selected_entry: str = temp_list[response]

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
