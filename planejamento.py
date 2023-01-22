import calendar

'''
#Input do ano e do mês que se deseja gerar o calendário
ano = int(input("Ano: "))
mês = int(input("Mês: "))

yy = 2023
mm = 2

print(calendar.month(yy, mm))
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

#Só para não fechar no cmd
input()