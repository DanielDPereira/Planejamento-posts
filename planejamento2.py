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

#Segunda = 0, Terça = 1, Quarta = 2, Quinta = 3, Sexta = 4, Sabádo = 5, Domingo = 6
#Segunda - ODS ou Confirma - Daniel Dias
#Terça - Explica - Gabriel Espildora
#Quarta - Explica ou Alerta - Anny
#Quinta - Explica - Daniel Sega
#Sexta - Indica ou Entrevista - Gabriella

dias_de_post_semana = [0,1,2,3,4]

#Loop for para ver quais dias do mês terão posts
dia = 1
dias_de_post = []
for i in range(Último_dia_do_mês):
    dia_semana = calendar.weekday(ano, mês, dia)
    if dia_semana in dias_de_post_semana:
        dias_de_post.append(dia)
    dia += 1

print(dias_de_post)    