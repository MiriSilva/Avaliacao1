
medias = []
notas =  []
for x in range(10):
       for j in range(0, 4): 
              nota = float(input("informe as Notas dos alunos:"))
              notas.append(nota) 
              media = sum(notas)/4

              medias.append(media)
quant = 0
for x in medias:
  if x >= 7:
    quant+=1
print("Quantidade de médias >= 7:",quant)