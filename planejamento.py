import calendar

#Input do ano e do mês que se deseja gerar o calendário
ano = int(input("Ano: "))
mês = int(input("Mês: "))

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

print("Segunda = 0, Terça = 1, Quarta = 2, Quinta = 3, Sexta = 4, Sabádo = 5, Domingo = 6")

#Segunda = 0, Terça = 1, Quarta = 2, Quinta = 3, Sexta = 4, Sabádo = 5, Domingo = 6
dias_desejados_input = input('Insira os dias da semana de posts (separe com uma ","): ')

# Transformando os dias em um array de string (que vai ser convertido pra número depois)
dias_desejados_array = dias_desejados_input.split(',')

dia_vídeo = int(input("Dia da semana onde será postado vídeo: "))

# Passando por cada elemento da lista, transformando em números e adicioando
# à uma nova lista que só vai ter números
dias_desejados1 = []

for elemento in dias_desejados_array:
    dias_desejados_convertido_em_numero = int(elemento)

    # adicionando o numero dos dias no array
    dias_desejados1.append(dias_desejados_convertido_em_numero)
        
#Loop for para ver quais dias do mês são do dia da semana sejados
dia = 1
dias_de_post = []
for i in range(Último_dia_do_mês):
    dia_semana = calendar.weekday(ano, mês, dia)
    if dia_semana in dias_desejados1:
        dias_de_post.append(dia)
    dia += 1

#Loop for para selecionar os dias que deverão ter vídeos
dia = 1
dias_de_post_vídeo = []
for i in range(Último_dia_do_mês):
    dia_semana = calendar.weekday(ano, mês, dia)
    if dia_semana == dia_vídeo:
        dias_de_post_vídeo.append(dia)
    dia += 1

#Post do dia

print("Explica = 0, Confirma = 1, Alerta = 2, ODS = 3, Indica = 4, Vídeo = 5")

#Explica = 0, Confirma = 1, Alerta = 2, ODS = 3, Indica = 4, Vídeo = 5
Tipos_de_post = ["Explica", "Confirma", "Alerta", "ODS", "Indica", "Vídeo"]

Tipos_de_post_sem_vídeo = ["Explica", "Confirma", "Alerta", "ODS", "Indica"]

contador_de_post_para_cada_dia = int(input("Tipo do último post: ")) + 1

if contador_de_post_para_cada_dia >= len(Tipos_de_post):
    contador_de_post_para_cada_dia = 0

#Print dos dias que terão post e o tipo
for i in dias_de_post:
    
    if i in dias_de_post_vídeo:
            
        if mês < 10:
            if i < 10:
                print("0"+str(i) + "/"+"0"+str(mês)+" Vídeo")
            else:
                print(str(i) + "/"+"0"+str(mês)+" Vídeo")
        else:
            if i < 10:
                print("0"+str(i) + "/"+str(mês)+" Vídeo")
            else:
                print(str(i) + "/"+str(mês)+" Vídeo")
    else:        
    
        if mês < 10:
            if i < 10:
                print("0"+str(i) + "/"+"0"+str(mês)+" "+Tipos_de_post_sem_vídeo[contador_de_post_para_cada_dia])
            else:
                print(str(i) + "/"+"0"+str(mês)+" "+Tipos_de_post_sem_vídeo[contador_de_post_para_cada_dia])
        else:
            if i < 10:
                print("0"+str(i) + "/"+str(mês)+" "+Tipos_de_post_sem_vídeo[contador_de_post_para_cada_dia])
            else:
                print(str(i) + "/"+str(mês)+" "+Tipos_de_post_sem_vídeo[contador_de_post_para_cada_dia])
            
    contador_de_post_para_cada_dia += 1
    if contador_de_post_para_cada_dia >= len(Tipos_de_post_sem_vídeo):
        contador_de_post_para_cada_dia = 0

#Só para não fechar no cmd
input()