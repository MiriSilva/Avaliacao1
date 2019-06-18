salario=int(input("informe seu salário:"))
if (salario=="280"):
    aumento = salario*0.2
if (280>=salario<=700):
    aumento = salario*0.15
if (700>=salario<=1500):
    aumento = salario*0.1
if (salario>=1500):
    aumento = salario*0.05
print("seu salario era:", salario)
print("seu salario apos o aumento é", (salario+aumento))

