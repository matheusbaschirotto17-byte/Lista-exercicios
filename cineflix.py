import json
import banco_streaming
from tempo import formatar_duracao


def ler_inteiro(mensagem, minimo=1):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_perfil():
    while True:
        perfil = input("Nome do perfil: ").strip()
        if perfil:
            return perfil
        print("O nome do perfil não pode ficar vazio.")


conn = banco_streaming.conectar()
perfil = ler_perfil()

while True:
    print(f"\n===== CINEFLIX ({perfil}) =====")
    print("1 - Ver catálogo")
    print("2 - Registrar que assisti")
    print("3 - Meu histórico")
    print("4 - Mais assistidos")
    print("5 - Tempo assistido por perfil")
    print("6 - Exportar relatório JSON")
    print("7 - Trocar de perfil")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        for t in banco_streaming.catalogo(conn):
            idade = "L" if t[6] == 0 else str(t[6])
            print(f"{t[0]:2}. {t[1]:25} {t[2]:8} {t[3]:15} {t[4]} {idade:>3} nota {t[7]:.1f}")

    elif opcao == "2":
        titulo_id = ler_inteiro("Id do título: ", 1)
        minutos = ler_inteiro("Quantos minutos você assistiu? ", 1)
        if banco_streaming.registrar(conn, perfil, titulo_id, minutos):
            print("Registrado!")
        else:
            print("Não existe título com esse id.")

    elif opcao == "3":
        registros = banco_streaming.historico(conn, perfil)
        total = 0
        for data, titulo, minutos in registros:
            print(f"{data} {titulo:30} {formatar_duracao(minutos)}")
            total += minutos
        print(f"Total: {formatar_duracao(total)} em {len(registros)} sessões")

    elif opcao == "4":
        registros = banco_streaming.mais_assistidos(conn)
        if not registros:
            print("Ainda não há visualizações.")
        for i, (titulo, vezes) in enumerate(registros, 1):
            print(f"{i}º {titulo:30} {vezes} vez(es)")

    elif opcao == "5":
        registros = banco_streaming.tempo_por_perfil(conn)
        if not registros:
            print("Ainda não há visualizações.")
        for nome, minutos in registros:
            print(f"{nome:20} {formatar_duracao(minutos)}")

    elif opcao == "6":
        relatorio = banco_streaming.dados_relatorio(conn)
        with open("relatorio.json", "w", encoding="utf-8") as arquivo:
            json.dump(relatorio, arquivo, ensure_ascii=False, indent=2)
        print(f'relatorio.json gravado ({len(relatorio["mais_assistidos"])} títulos, {len(relatorio["tempo_por_perfil"])} perfis).')

    elif opcao == "7":
        perfil = ler_perfil()

    elif opcao == "0":
        break
    else:
        print("Opção inválida.")

conn.close()
