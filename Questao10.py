Usuario = input("Insira o Usuário")
Senha = input("Insira a Senha")

while Senha == Usuario:
    Senha = input("Digite uma senha diferente do nome de usuário:")

print("Usuário:", Usuario, "Senha:", Senha)