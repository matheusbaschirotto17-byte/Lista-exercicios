def ler_inteiro(mensagem, minimo):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número inteiro maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")

print("=== EXCURSÃO DA ESCOLA ===")
quantidade_turmas = ler_inteiro("Quantas turmas vão participar? ", 1)

turmas = []
total_alunos = 0

for i in range(quantidade_turmas):
    nome = input(f"\nNome da turma {i + 1}: ").strip()
    while not nome:
        print("O nome não pode ficar vazio.")
        nome = input(f"Nome da turma {i + 1}: ").strip()

    inscritos = ler_inteiro(f"Inscritos na turma {nome}: ", 0)
    turmas.append((nome, inscritos))
    total_alunos += inscritos

professores = (total_alunos + 14) // 15
total_pessoas = total_alunos + professores
onibus = (total_pessoas + 43) // 44
lugares_sobram = onibus * 44 - total_pessoas
custo = onibus * 1800

print("\n=== RESUMO ===")
print(f"Alunos: {total_alunos}")
print(f"Professores acompanhantes: {professores}")
print(f"Total de pessoas: {total_pessoas}")
print(f"Ônibus necessários: {onibus} (sobram {lugares_sobram} lugares)")
print(f"Custo total: R$ {custo:.2f}")

if total_alunos > 0:
    print(f"Valor por aluno: R$ {custo / total_alunos:.2f}")
else:
    print("Valor por aluno: não há alunos inscritos.")

if turmas:
    maior = max(turmas, key=lambda turma: turma[1])
    print(f"Turma com mais inscritos: {maior[0]} ({maior[1]} alunos)")
