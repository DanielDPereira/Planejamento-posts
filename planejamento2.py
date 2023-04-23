import calendar
import PySimpleGUI as sg

#Input do ano e do mês que se deseja gerar o calendário
ano = int(input("Ano: "))
mês = int(input("Mês: "))

if mês == 1 or mês == 3 or mês == 5 or mês == 7 or mês == 8 or mês == 10 or mês == 12:
    Último_dia_do_mês = 31
elif mês == 2:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        Último_dia_do_mês = 29
    else:
        Último_dia_do_mês = 28
elif mês == 4 or mês == 6 or mês == 9 or mês == 11:
    Último_dia_do_mês = 30