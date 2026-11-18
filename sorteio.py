import random
from datetime import datetime
import utilidades

print(utilidades.linha("="))
print("SORTEIO DE BRINDES - FEIRA DE CIÊNCIAS")
print(utilidades.linha("="))
print("Digite os nomes dos participantes (Enter vazio para terminar).")

participantes = []
while True:
    nome = utilidades.ler_texto(f"Participante {len(participantes) + 1}: ", vazio=True)
    if not nome:
        break
    if nome.casefold() in [p.casefold() for p in participantes]:
        print(f"{nome} já está na lista.")
    else:
        participantes.append(nome)

if not participantes:
    print("Nenhum participante cadastrado.")
else:
    qtd = utilidades.ler_inteiro(
        f"\nQuantos brindes (1 a {len(participantes)})? ", 1, len(participantes)
    )

    brindes = []
    for i in range(qtd):
        brindes.append(utilidades.ler_texto(f"Brinde {i + 1}: "))

    ganhadores = random.sample(participantes, qtd)

    print("\n" + utilidades.linha("-"))
    print("Sorteio realizado em", datetime.now().strftime("%d/%m/%Y às %H:%M"))
    print(f"{len(participantes)} participantes, {qtd} brindes")
    print(utilidades.linha("-"))
    for brinde, ganhador in zip(brindes, ganhadores):
        print(f"{brinde:20} -> {ganhador}")
