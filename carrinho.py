def subtotal_item(preco, quantidade=1):
    return preco * quantidade


def aplicar_cupom(total, cupom):
    cupons = {"PROMO10": 10, "VOLTAASAULAS": 15, "BLACK25": 25}
    percentual = cupons.get(cupom.strip().upper(), 0)
    return total * (1 - percentual / 100), percentual


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0.0
    return valor


def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas
    return total * (1 + 0.02 * parcelas) / parcelas


def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", ".").replace("R$", "").strip())
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Digite um número válido.")


def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


print("=== LOJA VIRTUAL ===")
subtotal = 0

while True:
    produto = input("\nProduto (Enter para fechar o carrinho): ").strip()
    if produto == "":
        break

    preco = ler_float("Preço: R$ ")
    quantidade = ler_inteiro("Quantidade: ", 1, 999999)
    valor = subtotal_item(preco, quantidade)
    subtotal += valor
    print(f"  {quantidade} x {produto} = R$ {valor:.2f}   (carrinho: R$ {subtotal:.2f})")

cupom = input("\nCupom de desconto (Enter se não tiver): ")
com_desconto, percentual = aplicar_cupom(subtotal, cupom)

if cupom.strip() and percentual == 0:
    print("Cupom inválido. Nenhum desconto aplicado.")

desconto = subtotal - com_desconto
frete = calcular_frete(com_desconto)
total = com_desconto + frete
parcelas = ler_inteiro("Em quantas parcelas (1 a 12)? ", 1, 12)

print("\n=== NOTA ===")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: {percentual}% (R$ {desconto:.2f})")
print(f"Frete:     R$ {frete:.2f}")
print(f"Total:     R$ {total:.2f}")
print(f"Pagamento: {parcelas} x R$ {valor_parcela(total, parcelas):.2f}")
