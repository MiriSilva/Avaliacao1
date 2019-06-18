perguntas =["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

resposta = 0

for x in perguntas:
    resposta +=(input(x)=="s")

if resposta == 5:
    print("Assassino")
elif resposta >=3:
  print("Cúmplice")
elif resposta ==2:
  print("Suspeito")
else:
  print("Inocente")
  