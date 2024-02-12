class Colour:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    ORANGE = "\033[0;93m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    HIGHLIGHT = "\033[;7m"


def is_empty(item):
    if not item:
        return True
    else:
        return False


def create_indexed_list(todo_list: dict) -> list[str]:
    temp_list: list[str] = [x for x in todo_list.keys()]
    return temp_list


def print_indexed_list(temp_list: list):
    # To present the list with index
    print(Colour.BLUE, end="")

    for i in range(len(temp_list)):
        print(f"{i+1}. {temp_list[i]}")

    print(Colour.RESET, end="")
