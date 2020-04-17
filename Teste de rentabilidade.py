import os
os.system('clear')

print("Quais investimentos deseja comparar?\n")
Insves1 = input()
Capital = float(input("Capital investido em {}: R$".format(Insves1)).replace(",","."))
print("Obs: Em seguida será pedido a taxa de rentabilidade ao mês e ao ano, não é necessário informar ambas pois o calculo é automático. \n")
a=0
while (a==0):
    tax1am = input("Taxa de rentabilidade {} terá a.m  (em %): " .format(Insves1)).replace(",",".")
    tax1aa = input("Taxa de rentabilidade {} terá a.a  (em %): " .format(Insves1)).replace(",",".")
    if tax1aa == '' and tax1am == '':
        print("Houve um erro e não recebi taxa de rentabilidade a.m ou a.a. Por favor, tente novamente: \t")
    else:
        a=a+1


if tax1am == '':
    tax1am = (1 + float(tax1aa))**(1/12) - 1
else:
    tax1aa = (1 + float(tax1am))**(12/1) - 1

Tcap = str(input("Período de capitalização: ")).lower().split(' ')
#if Tcap[1]==None or Tcap[1]==IndexError()####################################
ir = str(input("Cobra IR? ")).lower()

if (Tcap[1]=="meses"):
    Tap = float(Tcap[0])
elif (Tcap[1]=="anos"):
    Tap = 12*float(Tcap[0])
else: 
    Tcap.append(' a')
    Tcap.replace("a","meses")
Montante_sem_IR = Capital*(1+float(tax1am))**Tap
Lucro_depois_do_IR = (Montante_sem_IR - Capital)*0.85
Montante_com_IR = Capital + Lucro_depois_do_IR

if (ir == "sim"):
    Montante_final = Capital + Lucro_depois_do_IR
    print("Valor final: %.2f", %Montante_fina))
else: 
    print("Valor final: %.2f", %Montante_sem_IR)

#Insves2 = input()
#tax2 = input("Qual a taxa de rentabilidade de {}" .format(Insves2))
