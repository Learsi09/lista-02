nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = "A"
    situacao = "APROVADO"
elif media >= 7.5:
    conceito = "B"
    situacao = "APROVADO"
elif media >= 6.0:
    conceito = "C"
    situacao = "APROVADO"
elif media >= 4.0:
    conceito = "D"
    situacao = "REPROVADO"
else:
    conceito = "E"
    situacao = "REPROVADO"

print("Notas: {} e {}".format(nota1, nota2))
print("Média: {:.1f}".format(media))
print("Conceito: {}".format(conceito))
print("Situação: {}".format(situacao))