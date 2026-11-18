from datetime import date
import multas

def ler_data(mensagem, hoje_se_vazio=False):
    while True:
        texto = input(mensagem).strip()
        if hoje_se_vazio and texto == "":
            return date.today()
        try:
            return multas.converter_data(texto)
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")


print("=== BALCÃO DE DEVOLUÇÕES ===")
livros = 0
com_atraso = 0
total_multas = 0

while True:
    titulo = input("\nTítulo do livro (Enter para encerrar): ").strip()
    if not titulo:
        break

    prevista = ler_data("Data prevista (dd/mm/aaaa): ")
    devolucao = ler_data("Data da devolução (Enter = hoje): ", True)

    dias = multas.dias_de_atraso(prevista, devolucao)
    multa = multas.valor_multa(dias)
    livros += 1
    total_multas += multa

    if dias > 0:
        com_atraso += 1
        print(f"'{titulo}' com {dias} dia(s) de atraso. Multa: R$ {multa:.2f}")
    else:
        print(f"'{titulo}' devolvido no prazo. Obrigado!")

print("\n=== FECHAMENTO DO DIA ===")
print(f"Livros devolvidos: {livros}")
print(f"Com atraso: {com_atraso}")
print(f"Total em multas: R$ {total_multas:.2f}")
