import functions
import time
import PySimpleGUI as gui

label = gui.Text('Type in a to-do:')
input_box = gui.InputText(tooltip='Enter to-do:',
                          key='todo')
add_button = gui.Button('Add')
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
quit_button = gui.Button('Quit')

window = gui.Window('To-do',
                    layout=[[label], [input_box, add_button], [quit_button]],
                    font=('Helvetica', 10))

while True:
    event, values = window.read()
    if event == 'Add':
        action = event + " " + values['todo']
        functions.add(action)

    elif event == 'Edit':
        somecode = 0

    elif event == 'Complete':
        somecode = 0

    elif event == 'Quit':
        break

    else:
        print('Something went wrong')
        break

window.close()
