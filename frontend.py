import functions
import time
import PySimpleGUI as sg

sg.theme('DarkTeal')
sg.set_options(font=('Jetbrains mono', 14))

label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip='Enter to-do:',
                         key='todo',
                         expand_x=True,
                         do_not_clear=False)
add_button = sg.Button('Add', bind_return_key=True)

list_box = sg.Listbox(values=functions.get_todos(), key='Selection',
                      expand_x=True, expand_y=True,
                      select_mode='single', enable_events=True)

edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
refresh_button = sg.Button('🔄',
                           font=('Jetbrains mono', 14, 'bold'),
                           tooltip="Refresh")

window = sg.Window('To-do',
                   size=(750, 400), resizable=True,
                   layout=[[label],
                           [input_box, add_button],
                           [list_box],
                           [refresh_button, edit_button, complete_button]])

while True:
    event, values = window.read()
    match event:
        case 'Add':
            new_todo = values['todo']
            functions.add_todo(new_todo)

        case '🔄':
            list_box.update(functions.get_todos())

        case 'Edit':
            if selected_todo is None:
                continue
            else:
                replacement_todo = values['todo']
                functions.replace_todo(selected_todo, replacement_todo)

        case 'Complete':
            if selected_todo is None:
                continue
            else:
                functions.complete_todo(selected_todo)

        case 'Quit':
            break

        case sg.WINDOW_CLOSED:
            print('The application window was closed.')
            break

        case 'Selection':
            selected_todo = list_box.get_indexes()[0]
            print(selected_todo)
            continue

        case _:
            print('Something went wrong')
            break

    list_box.update(functions.get_todos())

window.close()
