num_apples = int(input("Quantas maçãs você comprou? "))

if num_apples < 12:
    total_cost = num_apples * 1.30
else:
    total_cost = num_apples * 1.00

print("O custo total da compra é R$ {:.2f}".format(total_cost))