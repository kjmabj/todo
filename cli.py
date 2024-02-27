import functions
import time

print(f"Welcome to this simple to-do application. Your to-do changes will be written to ./{functions.FILEPATH}")
print("Will this push?")

now = time.strftime("%d.%m.%Y %H:%M:%S")
print(f"The current time is {now}\n")
print(functions.readme())

while True:
    user_command = input('Enter command: ')
    user_command = user_command.strip()

    if 'add' in user_command:
        functions.add(user_command)

    elif 'edit' in user_command:
        functions.edit(user_command)

    elif 'complete' in user_command:
        functions.complete(user_command)

    elif 'show' in user_command:
        functions.show()

    elif 'help' in user_command:
        print(functions.readme())
        functions.readme()

    elif 'exit' in user_command:
        break

    else:
        continue
