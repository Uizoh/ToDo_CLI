def create_indexed_list(todo_list: dict) -> list[str]:

    temp_list: list[str] = [x for x in todo_list.keys()]
    return temp_list


def print_indexed_list(temp_list: list):
    # To present the list with index
    for i in range(len(temp_list)):
        print(f"{i+1}. {temp_list[i]}")
