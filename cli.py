import functions
import time

print(f"---\n"
      f"Welcome to this simple to-do application. Your to-do changes will be written to ./{functions.FILEPATH}\n"
      f"---\n")

now = time.strftime("%d.%m.%Y %H:%M:%S")
print(f"The current time is {now}\n")

todos = functions.get_todos()

print("Initial list of todos:\n")
for i, index in enumerate(todos):
    print(f"{i + 1}. {todos[i]}")
print()

while True:
    user_command = input('Enter command: ')
    user_command = user_command.strip()

    if 'add' in user_command:
        todo = user_command[4:]
        functions.add_todo(todo)

    elif 'edit' in user_command:
        index = int(user_command[5:]) - 1
        replacement_todo = input('Enter replacement todo: ')
        print(index)
        print(replacement_todo)
        functions.replace_todo(index, replacement_todo)

    elif 'complete' in user_command:
        index = int(user_command[8:]) - 1
        functions.complete_todo(index)

    elif 'show' in user_command:
        todos = functions.get_todos()
        for i, index in enumerate(todos):
            print(f"{i+1}. {todos[i]}")

    elif 'exit' in user_command:
        break

    else:
        continue
