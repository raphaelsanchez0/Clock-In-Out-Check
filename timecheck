import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
#constants
time_input_size = (4,1)

layout = [  [sg.Text('TimeCheck',font = ("Helvetica",20))],
            [sg.Text('In:'), sg.InputText(size=time_input_size),sg.Text('Out:'),sg.InputText(size=time_input_size),sg.Button('+')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()