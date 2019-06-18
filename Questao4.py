x = float(input("Informe quanto ganha por hora:"))
y = float(input("Informe quantas horas trabalhadas no mês:"))

SB = (x*y)
IR = SB * 0.11 
INSS = SB* 0.08
SD = SB*0.05
SL = SB-(IR+INSS+SD)

print("Salário Bruto : R$",SB)
print("IR (11%) : R$",IR )
print("INSS (8%) : R$",INSS )
print("Sindicato ( 5%) : R$",SD )
print("Salário Liquido : R$",SL )