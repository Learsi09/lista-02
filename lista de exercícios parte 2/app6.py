valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    menor = valor2
    maior = valor1
else:
    menor = valor1
    maior = valor2

print("Os valores em ordem crescente são: {:.2f} e {:.2f}".format(menor, maior))