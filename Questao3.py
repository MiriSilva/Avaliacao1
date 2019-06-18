h = float(input("informe sua altura: "))
s = (input("informe seu sexo: m ou f: "))

if s=="m":
    IMC = (72.7*h) - 58
else:
    IMC = (62.1*h) - 44.7

print ("Seu peso ideal é :", IMC)
