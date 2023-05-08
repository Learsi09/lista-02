quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2

if quantidade_atual >= quantidade_media:
    situacao = "Não efetuar compra"
else:
    situacao = "Efetuar compra"

print("A quantidade média em estoque é de {}. {}".format(quantidade_media, situacao))