import os

FILEPATH = 'files/todos.txt'
file_exists = os.path.exists(FILEPATH)

if not file_exists:
    os.mkdir('files')
    file_check = open(FILEPATH, 'w+')
    file_check.close()


def readme():
    return ('┌────────────────────────┬─────────────────────────────────────────┐\n'
            '│Command                 │ Description                             │\n'
            '│────────────────────────┼─────────────────────────────────────────│\n'
            '│show                    │ Show current list of to-dos             │\n'
            '│add <to-do>             │ Adds new <to-do>                        │\n'
            '│edit <to-do number>     │ Edits the to-do                         │\n'
            '│complete <to-do number> │ To complete (remove) to-do              │\n'
            '│help                    │ Display this list of commands.          │\n'
            '└────────────────────────┴─────────────────────────────────────────┘\n')


def add(action):
    todo = action[4:]

    if todo != "":
        with open(FILEPATH, 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open(FILEPATH, 'w') as file:
            file.writelines(todos)

    else:
        return


def show():
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()

    if not todos:
        print('There is nothing to show (to-do list is empty).')

    else:
        for i, item in enumerate(todos):
            print(f"{i + 1}. {item.strip()}")

    # List comprehension way
    # new_todos = [item.strip('\n') for item in todos]


def get_todos():
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()

    if not todos:
        return

    else:
        return todos


def edit(action):
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    number = 0

    try:
        number = int(action[5:]) - 1
        test = todos[number] + "1"

    except ValueError:
        print('Input is invalid. Must be \'edit\' followed by a number.')
    except IndexError:
        print(f'Item with the number {number + 1} does not exist.')
    else:
        if todos[number]:
            new_todo = input('Enter a replacement to-do: ')
            todos[number] = new_todo + '\n'

            with open(FILEPATH, 'w') as file:
                file.writelines(todos)
    finally:
        return


def complete(action):
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    number = 0

    try:
        number = int(action[9:]) - 1
        index_test = todos[number]

    except ValueError:
        print('Input is invalid. Must be \'complete\' followed by a number.')

    except IndexError:
        print(f'Item with the number {number + 1} does not exist.')

    else:
        confirmation = input(f'Are you sure you want to complete the task \'{todos[number].strip('\n')}\'? (y/n): ')
        if confirmation == 'y':
            todos.pop(number)
            with open(FILEPATH, 'w') as file:
                file.writelines(todos)
        elif confirmation == "n":
            print(f"Deletion of \'{todos[number].strip('\n')}\' from to-do was cancelled.")
        else:
            return


if __name__ == '__main__':
    print(show())
