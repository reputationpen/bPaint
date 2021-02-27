import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Pretty cool')],
          [sg.Input('What if i put text here')],
          [sg.Button('Read'), sg.Exit()],
          [sg.Button('More Changes')]]

window = sg.Window('Bro I made changes', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event, values)

window.close()
