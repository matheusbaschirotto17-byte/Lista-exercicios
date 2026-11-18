from datetime import datetime


def converter_data(texto):
    return datetime.strptime(texto, "%d/%m/%Y").date()


def dias_de_atraso(data_prevista, data_devolucao):
    dias = (data_devolucao - data_prevista).days
    return max(0, dias)


def valor_multa(dias, por_dia=1.50, maximo=30.00):
    return min(dias * por_dia, maximo)


if __name__ == "__main__":
    prevista = converter_data("05/11/2026")
    devolucao = converter_data("10/11/2026")
    print(dias_de_atraso(prevista, devolucao))
    print(valor_multa(5))
    print(valor_multa(40))
    print(valor_multa(5, por_dia=2))
