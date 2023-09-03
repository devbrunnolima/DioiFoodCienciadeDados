def calcular_valor_com_desconto(pedidos, cupom_desconto):
    total = 0
    for pedido in pedidos:
        total += pedido[1]

    if cupom_desconto == "10%":
        total *= 0.9
    elif cupom_desconto == "20%":
        total *= 0.8

    return total


def main():
    n = int(input())

    pedidos = []
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        pedidos.append((nome, valor))

    cupom_desconto = input()

    valor_total_com_desconto = calcular_valor_com_desconto(pedidos, cupom_desconto)

    print(f"Valor total: {valor_total_com_desconto:.2f}")


if __name__ == "__main__":
    main()