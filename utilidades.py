def ler_texto(mensagem, vazio=False):
    while True:
        texto = input(mensagem).strip()
        if texto or vazio:
            return texto
        print("Este campo não pode ficar vazio.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"O mínimo é {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"O máximo é {maximo}.")
            else:
                return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def linha(caractere="-", tamanho=40):
    return caractere * tamanho


if __name__ == "__main__":
    print(linha("="))
    print(ler_texto("Nome: "))
    print(ler_inteiro("Quantidade: ", 1, 10))
    print(linha("-", 20))
