
area = int(input("informe a area em metros quadrados a ser pintada:"))
litros=area/3
preco = 80.0
capacidade = 18
latas = litros / capacidade
total = latas * preco

print ("latas de tinta nescessarias:", latas)
print ("O preco total é de: R$", total)