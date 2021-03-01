import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Pretty cool')],
          [sg.Input()],
          [sg.Button('Read')]]

window = sg.Window('Bro I made changes', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(event, values)

window.close()
