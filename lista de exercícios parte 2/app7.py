conta = int(input("Digite o número da conta do cliente: "))
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    situacao = "Saldo Positivo"
else:
    situacao = "Saldo Negativo"

print("O saldo atual da conta {} é de {:.2f}. {}".format(conta, saldo_atual, situacao))