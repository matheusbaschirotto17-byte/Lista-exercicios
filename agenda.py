import json
import os
from datetime import datetime

ARQUIVO = "shows.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        print("Não foi possível ler shows.json. Agenda iniciada vazia.")
        return []


def salvar(shows):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(shows, arquivo, ensure_ascii=False, indent=2)


def ler_data():
    while True:
        texto = input("Data (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(texto, "%d/%m/%Y")
            return texto
        except ValueError:
            print("Data inválida. Digite no formato dd/mm/aaaa.")


def ler_float(mensagem, minimo=0):
    while True:
        try:
            valor = float(input(mensagem).replace(",", ".").replace("R$", "").strip())
            if valor >= minimo:
                return valor
            print(f"Digite um valor maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número válido.")


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ordenar(shows):
    return sorted(shows, key=lambda s: datetime.strptime(s["data"], "%d/%m/%Y"))


def listar(shows):
    if not shows:
        print("Nenhum show cadastrado.")
        return
    for i, show in enumerate(ordenar(shows), 1):
        situacao = "ESGOTADO" if show["ingressos"] == 0 else f'{show["ingressos"]} ingressos'
        print(f'{i}. {show["data"]:12} {show["artista"]:25} {show["cidade"]:18} R$ {show["preco"]:8.2f} {situacao}')


shows = carregar()
print(f"Agenda carregada: {len(shows)} shows.")

while True:
    print("\n===== AGENDA DE SHOWS =====")
    print("1 - Listar shows")
    print("2 - Cadastrar show")
    print("3 - Shows em uma cidade")
    print("4 - Vender ingressos")
    print("5 - Remover show")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        listar(shows)

    elif opcao == "2":
        artista = input("Artista/banda: ").strip()
        cidade = input("Cidade: ").strip()
        while not artista or not cidade:
            print("Artista e cidade são obrigatórios.")
            artista = input("Artista/banda: ").strip()
            cidade = input("Cidade: ").strip()
        data = ler_data()
        preco = ler_float("Preço do ingresso: R$ ", 0.01)
        ingressos = ler_inteiro("Ingressos disponíveis: ", 0)
        shows.append({"artista": artista, "cidade": cidade, "data": data,
                      "preco": preco, "ingressos": ingressos})
        salvar(shows)
        print("Show cadastrado e agenda salva.")

    elif opcao == "3":
        cidade = input("Cidade: ").strip()
        encontrados = [s for s in ordenar(shows) if cidade.casefold() in s["cidade"].casefold()]
        if encontrados:
            listar(encontrados)
        else:
            print("Nenhum show encontrado nessa cidade.")

    elif opcao == "4":
        ordenados = ordenar(shows)
        if not ordenados:
            print("Nenhum show cadastrado.")
            continue
        for i, show in enumerate(ordenados, 1):
            situacao = "ESGOTADO" if show["ingressos"] == 0 else f'{show["ingressos"]} ingressos'
            print(f'{i}. {show["data"]} {show["artista"]:25} {show["cidade"]:18} R$ {show["preco"]:8.2f} {situacao}')
        numero = ler_inteiro("Número do show: ", 1)
        if numero > len(ordenados):
            print("Número de show inválido.")
            continue
        quantidade = ler_inteiro("Quantos ingressos? ", 1)
        show = ordenados[numero - 1]
        if quantidade > show["ingressos"]:
            print(f'Só restam {show["ingressos"]} ingressos.')
        else:
            show["ingressos"] -= quantidade
            salvar(shows)
            print(f'Venda: {quantidade} x R$ {show["preco"]:.2f} = R$ {quantidade * show["preco"]:.2f}')

    elif opcao == "5":
        ordenados = ordenar(shows)
        if not ordenados:
            print("Nenhum show cadastrado.")
            continue
        listar(shows)
        numero = ler_inteiro("Número do show: ", 1)
        if numero > len(ordenados):
            print("Número de show inválido.")
            continue
        removido = ordenados[numero - 1]
        shows.remove(removido)
        salvar(shows)
        print(f'Show de {removido["artista"]} removido.')

    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
