nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))

media = (nota1 + nota2) / 2

if media >= 6.0:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print("Média: {:.1f}".format(media))
print("Situação: {}".format(situacao))