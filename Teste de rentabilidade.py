import os
os.system('clear')

print("Quais investimentos deseja comparar?\n")
Insves1 = input()
Capital = float(input("Capital investido em {}: R$".format(Insves1)).replace(",","."))
print("Obs: Em seguida será pedido a taxa de rentabilidade ao mês e ao ano, não é necessário informar ambas pois o calculo é automático. \n")

while True:
    tax1am = input("Taxa de rentabilidade {} terá a.m  (em %): " .format(Insves1)).replace(",",".")
    tax1aa = input("Taxa de rentabilidade {} terá a.a  (em %): " .format(Insves1)).replace(",",".")
    if tax1aa == '' and tax1am == '':
        print("Houve um erro e não recebi taxa de rentabilidade a.m ou a.a. Por favor, tente novamente: \t")
    else:
        break

if tax1am == '':
    tax1am = (1 + float(tax1aa)/100)**(1/12) - 1
else:
    tax1aa = (1 + float(tax1am)/100)**(12/1) - 1

while True:
    Tcap = str(input("Período de capitalização(ex: 5 meses ou 2 anos ou 1 ano e 2 meses): ")).lower().replace("mês","mes").replace("meses","mes").replace("anos","ano").split()
    if (Tcap[0] == ''):
        print("Você não informou nenhum período de capitalização, tente novamente.\n")
    else:
        if len(Tcap)==1:
            Tcap.append('a')
        break
if "mes" and "ano" in Tcap:
    Tap = float(Tcap[0])*12+float(Tcap[3])
elif (Tcap[1]=="ano"):
    Tap = 12*float(Tcap[0])
elif (Tcap[1]=="mes"):
    Tap = float(Tcap[0])
else: 
    Tcap[1].replace("a","meses")
    Tap = float(Tcap[0])

ir = str(input("Cobra IR? ")).lower()

Montante_sem_IR = Capital*(1+float(tax1am))**Tap
Lucro_depois_do_IR = (Montante_sem_IR - Capital)*0.85
Montante_com_IR = Capital + Lucro_depois_do_IR

if (ir == "sim"):
    Montante_final = Capital + Lucro_depois_do_IR
    print("Valor final: {:.2f}" .format(Montante_final))
else: 
    print("Valor final: {:.2f}" .format(Montante_sem_IR))

#Insves2 = input()def Calcula_rendimento(Var):
#     if Var == ''

#tax2 = input("Qual a taxa de rentabilidade de {}" .format(Insves2))


# def Calcula_rendimento(Var):
#     if Var == ''
