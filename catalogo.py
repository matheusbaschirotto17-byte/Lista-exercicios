import json


def carregar_catalogo():
    with open("catalogo.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def mostrar_titulo(t):
    idade = "L" if t["classificacao"] == 0 else str(t["classificacao"])
    print(f'{t["id"]:2}. {t["titulo"]:25} {t["tipo"]:8} {t["genero"]:15} {t["ano"]:4} {idade:>3} nota {t["nota"]:.1f}')


def listar_tudo(catalogo):
    for titulo in catalogo:
        mostrar_titulo(titulo)


def filtrar_por_genero(catalogo, genero):
    return [t for t in catalogo if t["genero"].casefold() == genero.casefold()]


def buscar_titulo(catalogo, texto):
    return [t for t in catalogo if texto.casefold() in t["titulo"].casefold()]


def titulos_por_idade(catalogo, idade):
    return [t for t in catalogo if t["classificacao"] <= idade]


def mais_bem_avaliados(catalogo, quantidade):
    return sorted(catalogo, key=lambda t: t["nota"], reverse=True)[:quantidade]


def estatisticas(catalogo):
    filmes = sum(1 for t in catalogo if t["tipo"].casefold() == "filme")
    series = sum(1 for t in catalogo if t["tipo"].casefold() == "série")
    media = sum(t["nota"] for t in catalogo) / len(catalogo) if catalogo else 0
    generos = sorted(set(t["genero"] for t in catalogo))
    print(f"Títulos: {len(catalogo)} (filmes: {filmes}, séries: {series})")
    print(f"Nota média: {media:.2f}")
    print("Gêneros:", ", ".join(generos))


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


catalogo = carregar_catalogo()
print(f"Catálogo carregado: {len(catalogo)} títulos.")

while True:
    print("\n===== CINEFLIX =====")
    print("1 - Listar tudo")
    print("2 - Filtrar por gênero")
    print("3 - Buscar título")
    print("4 - Títulos para a minha idade")
    print("5 - Mais bem avaliados")
    print("6 - Estatísticas")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        listar_tudo(catalogo)
    elif opcao == "2":
        generos = sorted(set(t["genero"] for t in catalogo))
        print("Gêneros:", ", ".join(generos))
        genero = input("Gênero: ").strip()
        encontrados = filtrar_por_genero(catalogo, genero)
        for t in encontrados:
            mostrar_titulo(t)
        if not encontrados:
            print("Nenhum título encontrado.")
    elif opcao == "3":
        texto = input("Parte do título: ").strip()
        encontrados = buscar_titulo(catalogo, texto)
        for t in encontrados:
            mostrar_titulo(t)
        if not encontrados:
            print("Nenhum título encontrado.")
    elif opcao == "4":
        idade = ler_inteiro("Sua idade: ")
        encontrados = titulos_por_idade(catalogo, idade)
        for t in encontrados:
            mostrar_titulo(t)
    elif opcao == "5":
        texto = input("Quantos (Enter = 5)? ").strip()
        if texto == "":
            quantidade = 5
        else:
            try:
                quantidade = int(texto)
                if quantidade < 1:
                    raise ValueError
            except ValueError:
                print("Digite um número inteiro maior que zero.")
                continue
        for t in mais_bem_avaliados(catalogo, quantidade):
            mostrar_titulo(t)
    elif opcao == "6":
        estatisticas(catalogo)
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
