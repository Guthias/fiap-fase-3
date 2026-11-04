# Análise de energia: compara a geração com o consumo e gera uma ação.


def calcular_saldo(geracao, consumo):
    if geracao < 0 or consumo < 0:
        raise ValueError("Geração e consumo não podem ser negativos")
    return geracao - consumo


def analisar_energia(geracao, consumo, espaco_livre=None):
    saldo = calcular_saldo(geracao, consumo)
    if saldo < 0:
        return "ALERTA: consumo maior que geração"
    elif saldo > 0:
        if espaco_livre is not None and espaco_livre <= 0:
            return "AVISO: excedente sem espaço de armazenamento"
        return "SUGESTÃO: armazenar energia excedente"
    else:
        return "EQUILÍBRIO: geração igual ao consumo"


if __name__ == "__main__":
    print(analisar_energia(40, 70))
    print(analisar_energia(80, 30))
    print(analisar_energia(80, 30, espaco_livre=0))
    print(analisar_energia(50, 50))