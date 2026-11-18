nomes = []
pesos = []
total = 0

print("=== MOCHILA DE CAMPING ===")
print("Digite os itens. Para terminar, digite FIM.")

while True:
    nome = input("\nItem: ").strip()
    if nome.upper() == "FIM":
        break
    if not nome:
        print("Digite o nome do item.")
        continue

    while True:
        try:
            peso = float(input("Peso (kg): ").replace(",", "."))
            if peso <= 0:
                print("Digite um peso maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número, por exemplo 1.5.")

    nomes.append(nome)
    pesos.append(peso)
    total += peso

    if total > 15:
        print(f"Atenção: a mochila já tem {total:.1f} kg (limite 15 kg)!")

print("\n=== RESUMO ===")
if len(nomes) == 0:
    print("A mochila está vazia.")
else:
    for i in range(len(nomes)):
        print(f"{i + 1}. {nomes[i]:25} {pesos[i]:.1f} kg")

    print(f"Itens: {len(nomes)}")
    print(f"Peso total: {total:.1f} kg")
    print(f"Peso médio: {total / len(pesos):.2f} kg")

    maior = pesos.index(max(pesos))
    print(f"Item mais pesado: {nomes[maior]} ({pesos[maior]:.1f} kg)")

    if total > 15:
        print(f"Tire {total - 15:.1f} kg da mochila para ficar dentro do limite.")
    else:
        print(f"Ainda cabem {15 - total:.1f} kg na mochila.")
