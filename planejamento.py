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
        
print(Último_dia_do_mês)
            
print(calendar.month(ano, mês))

#Loop for para ver quais dias do mês são do dia da semana sejados
dia = 1
dias_de_post = []
for i in range(Último_dia_do_mês):
    dia_semana = calendar.weekday(ano, mês, dia)
    

#0 = segunda, 1 = terça, 2 = quarta, 3 = quinta, 4 = sexta, 5 = sabádo, 6 = domingo



'''
def Ordena_dic(d): #<--Função para ordenar o dicionário original
    return dict(sorted(d.items(), key=lambda t:t[1]))

#Input dos valores que serão inseridos no dicionário original
V_Alerta1 = int(input("V Alerta "))
V_Confirma1 = int(input("V Confirma "))
V_Explica1 = int(input("V Explica "))
V_Indica1 = int(input("V Indica "))
Verus_ODS1 = int(input("V ODS "))

#Criando dicionário original
dict_posts1 = {
    "V_Alerta": V_Alerta1,
    "V_Confirma": V_Confirma1,
    "V_Explica": V_Explica1,
    "V_Indica": V_Indica1,
    "V_ODS": Verus_ODS1
    }

print(dict_posts1)

#Ordenando o dicionário original e criando em um segund dicionário, já ordenado
dict_posts2 = Ordena_dic(dict_posts1)

print(dict_posts2)
'''

#Só para não fechar no cmd
input()