import banco_estoque

def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_preco(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", ".").replace("R$", "").strip())
            if valor > 0:
                return valor
            print("Digite um preço maior que zero.")
        except ValueError:
            print("Digite um preço válido.")


def mostrar(produtos):
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    print(f"{'Id':>3} {'Produto':30} {'Categoria':15} {'Preço':>9} {'Qtd':>5}")
    for p in produtos:
        aviso = " <- repor" if p[4] < p[5] else ""
        print(f"{p[0]:3} {p[1]:30} {p[2]:15} {p[3]:9.2f} {p[4]:5}{aviso}")


conn = banco_estoque.conectar()

while True:
    print("\n===== ESTOQUE - LOJA DE CAMPING =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar por nome")
    print("4 - Entrada (chegou mercadoria)")
    print("5 - Saída (venda)")
    print("6 - Produtos para repor")
    print("7 - Valor total do estoque")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        nome = input("Nome: ").strip()
        categoria = input("Categoria: ").strip()
        while not nome or not categoria:
            print("Nome e categoria são obrigatórios.")
            nome = input("Nome: ").strip()
            categoria = input("Categoria: ").strip()
        preco = ler_preco("Preço: R$ ")
        quantidade = ler_inteiro("Quantidade inicial: ", 0)
        minimo = ler_inteiro("Estoque mínimo: ", 0)
        id_produto = banco_estoque.cadastrar(conn, nome, categoria, preco, quantidade, minimo)
        print(f"Produto cadastrado. Id: {id_produto}")

    elif opcao == "2":
        mostrar(banco_estoque.listar(conn))

    elif opcao == "3":
        texto = input("Parte do nome: ").strip()
        mostrar(banco_estoque.buscar(conn, texto))

    elif opcao == "4":
        id_produto = ler_inteiro("Id do produto: ", 1)
        quantidade = ler_inteiro("Quantidade que chegou: ", 1)
        if banco_estoque.entrada(conn, id_produto, quantidade):
            print("Entrada registrada.")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        id_produto = ler_inteiro("Id do produto: ", 1)
        quantidade = ler_inteiro("Quantidade vendida: ", 1)
        print(banco_estoque.saida(conn, id_produto, quantidade))

    elif opcao == "6":
        mostrar(banco_estoque.estoque_baixo(conn))

    elif opcao == "7":
        print(f"Valor total em estoque: R$ {banco_estoque.valor_total(conn):.2f}")

    elif opcao == "0":
        break
    else:
        print("Opção inválida.")

conn.close()
