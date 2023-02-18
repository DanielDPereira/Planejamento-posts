import PySimpleGUI as sg
    
sg.theme('DarkPurple1')   # Add a touch of color
# All the stuff inside your wi
# ndow.
layout = [  [sg.Text('Planejamento posts')],
            [sg.Text('Ano:')],
            [sg.InputText()],
            [sg.Text('Mês:')],
            [sg.InputText()],
            [sg.Text('Segunda = 0, Terça = 1, Quarta = 2, Quinta = 3, Sexta = 4, Sabádo = 5, Domingo = 6')],
            [sg.Text('Insira os dias da semana de posts (separe com uma ","): ')],
            [sg.InputText()],
            [sg.Text('Dias da semana onde serão postados vídeos: ')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Relatório', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break