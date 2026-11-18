def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60
    if horas > 0:
        return f"{horas}h{resto:02d}min"
    return f"{resto}min"


def tempo_total(duracoes):
    total = 0
    for duracao in duracoes:
        total += duracao
    return total


def dias_para_terminar(total_minutos, minutos_por_dia=120):
    return (total_minutos + minutos_por_dia - 1) // minutos_por_dia


def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    if total_minutos <= 900:
        return "Média"
    return "Intensa"


def ler_inteiro(mensagem, minimo):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


print("=== MARATONA DE SÉRIE ===")
serie = input("Nome da série: ").strip()
while not serie:
    serie = input("Digite o nome da série: ").strip()

temporadas = ler_inteiro("Quantas temporadas? ", 1)
duracoes = []

for i in range(1, temporadas + 1):
    episodios = ler_inteiro(f"Temporada {i} - número de episódios: ", 1)
    media = ler_inteiro(f"Temporada {i} - duração média do episódio (min): ", 1)
    duracoes.append(episodios * media)

total = tempo_total(duracoes)

print(f"\n=== {serie.upper()} ===")
for i, duracao in enumerate(duracoes, 1):
    print(f"Temporada {i}: {formatar_duracao(duracao)}")
print(f"Total: {formatar_duracao(total)} ({classificar_maratona(total)})")

por_dia = ler_inteiro("\nQuantos minutos por dia você pode assistir? ", 1)
print(f"Você termina {serie} em {dias_para_terminar(total, por_dia)} dias.")
print(f"Com 2 horas por dia (padrão), seriam {dias_para_terminar(total)} dias.")
