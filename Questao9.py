Morango = 2.50
Maças = 1.80

Qtd_morangos = float(input("quantos Kg de morangos deseja comprar?"))
Qtd_maças = float(input("quantos Kg de maças deseja comprar?"))

if (Qtd_morangos > 5):
    Morango = 2.20
if (Qtd_maças > 5):
    Maças = 1.50

Valor = ( Morango * Qtd_morangos) + (Maças * Qtd_maças)

if (Qtd_morangos + Qtd_maças) > 8 or Valor > 25.00:
    desconto = (Valor * 10) / 100
    ValorTotal = Valor - desconto

    print("O seu valor total foi %.2f" % ValorTotal, "R$")
else:
    print("O seu valor total foi %.2f" % Valor, "R$")
 