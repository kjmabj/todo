import os

FILEPATH = 'files/todos.txt'
file_exists = os.path.exists(FILEPATH)
print(file_exists)

if not file_exists:
    os.mkdir('files')
    file_check = open(FILEPATH, 'w+')
    file_check.close()


def add_todo(todo):
    if todo != "":
        with open(FILEPATH, 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open(FILEPATH, 'w') as file:
            file.writelines(todos)

    else:
        return


def replace_todo(index, todo):
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()

    if not todos:
        return

    else:
        todos[index] = todo + "\n"

        with open(FILEPATH, 'w') as file:
            file.writelines(todos)


def complete_todo(index):
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()

    if not todos:
        return

    else:
        todos.pop(index)

    with open(FILEPATH, 'w') as file:
        file.writelines(todos)


def get_todos():
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()

    if not todos:
        todos.append('My first todo')
        return todos

    else:
        index = -1
        for index, item in enumerate(todos):
            todos[index] = todos[index].strip('\n')
        return todos

