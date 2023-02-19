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
    
ano = int(values[0])
mês = int(values[1])

Último_dia_do_mês = 0
    
if mês == 1:
    Último_dia_do_mês = 31
elif mês == 2:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        Último_dia_do_mês = 29
    else:
        Último_dia_do_mês = 28
elif mês == 3:
    Último_dia_do_mês = 31
elif mês == 4:
    Último_dia_do_mês = 30
elif mês == 5:
    Último_dia_do_mês = 31
elif mês == 6:
    Último_dia_do_mês = 30
elif mês == 7:
    Último_dia_do_mês = 31
elif mês == 8:
    Último_dia_do_mês = 31
elif mês == 9:
    Último_dia_do_mês = 30
elif mês == 10:
    Último_dia_do_mês = 31
elif mês == 11:
    Último_dia_do_mês = 30
elif mês == 12:
    Último_dia_do_mês = 31

dias_desejados_input = values[2]

# Transformando os dias em um array de string (que vai ser convertido pra número depois)
dias_desejados_array = dias_desejados_input.split(',')

dia_vídeo_input = values[3]

# Passando por cada elemento da lista, transformando em números e adicioando
# à uma nova lista que só vai ter números
dias_desejados1 = []